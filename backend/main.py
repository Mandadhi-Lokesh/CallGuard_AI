from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, List
import os


from feature_extraction import extract_features
from detector import detect_ai

app = FastAPI(
    title="CallGuard AI Voice Detection API",
    description="Detects whether a voice sample is AI-generated or human using strict API standards.",
    version="1.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Configuration ---
API_KEY_SECRET = "sk_test_123456789"  # In production, use env vars

# --- Models ---
class VoiceDetectionRequest(BaseModel):
    # Language is now optional/informational
    language: Optional[str] = Field(None, description="Optional: Tamil, English, Hindi, Malayalam, Telugu, etc.")
    # Relaxed format restriction
    audioFormat: str = Field(..., description="wav, mp3, m4a, ogg, etc.")
    audioBase64: str = Field(..., description="Base64 encoded audio")

class VoiceDetectionMetadata(BaseModel):
    audio_format: str
    language: str

class VoiceDetectionResponse(BaseModel):
    status: str
    confidence: int
    classified_based_on: List[str]
    metadata: VoiceDetectionMetadata

# --- Dependencies ---
async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API key or malformed request")
    return x_api_key

# --- Endpoints ---
@app.post("/api/voice-detection", response_model=VoiceDetectionResponse)
def detect_voice(
    request: VoiceDetectionRequest,
    api_key: str = Depends(verify_api_key)
):
    temp_wav_path = None
    try:
        # 1. Load ANY audio format (Universal Loader)
        from audio_utils import load_audio_any_format
        temp_wav_path = load_audio_any_format(request.audioBase64, format_hint=request.audioFormat)
        
        # 2. Extract features
        features = extract_features(temp_wav_path)
        
        # 3. Detect
        result = detect_ai(features)
        
        return {
            "status": result["status"],
            "confidence": result["confidence"],
            "classified_based_on": result["classified_based_on"],
            "metadata": {
                "audio_format": request.audioFormat,
                "language": "multi-language supported"
            }
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Server Error: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Internal audio processing error"
        )
    finally:
        if temp_wav_path and os.path.exists(temp_wav_path):
            try:
                os.remove(temp_wav_path)
            except:
                pass
