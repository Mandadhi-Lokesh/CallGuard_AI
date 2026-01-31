from fastapi import FastAPI, HTTPException, Header, Depends, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional
import io
from pydub import AudioSegment

# remove decode_base64_mp3 as we don't need it for direct upload
# from audio_utils import decode_base64_mp3
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
    language: str = Field(..., description="Tamil, English, Hindi, Malayalam, or Telugu")
    audioFormat: str = Field(..., pattern="^mp3$", description="Must be 'mp3'")
    audioBase64: str = Field(..., description="Base64 encoded MP3 audio")

class VoiceDetectionResponse(BaseModel):
    status: str
    language: str
    classification: str
    confidenceScore: float
    explanation: str

# --- Dependencies ---
async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY_SECRET:
        raise HTTPException(status_code=401, detail="Invalid API key or malformed request")
    return x_api_key

# --- Endpoints ---
# --- Endpoints ---
@app.post("/api/voice-detection", response_model=VoiceDetectionResponse)
async def detect_voice(
    file: UploadFile = File(...),
    language: str = Form(...),
    api_key: str = Depends(verify_api_key)
):
    try:
        # Log reception
        print(f"Received file: {file.filename}, Size: {file.size} bytes, Content-Type: {file.content_type}")

        # Validate file type
        if not file.filename.lower().endswith(('.mp3', '.wav')):
             raise HTTPException(status_code=400, detail="Only .mp3 and .wav files are supported")

        # Read file
        audio_bytes = await file.read()
        
        # Create BytesIO object for compatibility with existing utils
        import io
        wav_io = io.BytesIO(audio_bytes)
        # Note: If existing utils specifically expect mp3 bytes to be decoded, 
        # we might need to adjust, but let's assume they handle the stream or bytes.
        # Looking at original code: decode_base64_mp3 returned a wav_io. 
        # We need to see if we need to decode MP3 to WAV here.
        # If the uploaded file IS mp3, we might need to convert it to WAV if extract_features expects WAV.
        
        # Let's inspect imports to be sure, but for now assuming we plug into existing flow.
        # Ideally we replace decode_base64_mp3 with a direct conversion if needed.
        # But wait, the previous code called `decode_base64_mp3`.
        # I'll stick to a safe path: if it's MP3, convert to WAV.
        
        from pydub import AudioSegment
        try:
            if file.filename.lower().endswith('.mp3'):
                audio = AudioSegment.from_mp3(io.BytesIO(audio_bytes))
                wav_io = io.BytesIO()
                audio.export(wav_io, format="wav")
                wav_io.seek(0)
            else:
                 # Assume WAV
                wav_io = io.BytesIO(audio_bytes)
        except Exception as conversion_err:
             print(f"Conversion error: {conversion_err}")
             # Fallback or re-raise
             raise HTTPException(status_code=400, detail="Invalid audio file format")

        
        # Extract features
        features = extract_features(wav_io)
        
        # Detect
        result = detect_ai(features)
        
        return {
            "status": "success",
            "language": language,
            "classification": result["classification"],
            "confidenceScore": result["confidence"],
            "explanation": result["explanation"]
        }

    except ValueError as e:
        # Client error (e.g. invalid audio format)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Server Error: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal audio processing error"
        )
