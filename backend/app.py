from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time
import os

import hashlib

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# In-memory Cache for Extracted Features
FEATURE_CACHE = {}

@app.route('/analyze', methods=['POST'])
def analyze_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        # Save file (optional for hackathon, but good for demo realism)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Log incoming request details (User requirement)
        print(f"Received file: {file.filename}")
        print(f"File size: {os.path.getsize(filepath)} bytes")
        
        robustness_mode = request.form.get('robustness', 'false').lower() == 'true'

        
        # Feature Extraction
        import io
        import detector
        import feature_extraction
        import audio_utils

        # Caching Logic
        # Read file to compute hash
        with open(filepath, 'rb') as f:
            file_content = f.read()
        
        file_hash = hashlib.sha256(file_content).hexdigest()
        cache_key = file_hash

        # Check Cache
        cached_data = FEATURE_CACHE.get(cache_key)
        
        if cached_data:
            print(f"Cache Hit for {file_hash[:8]}... (robustness_mode={robustness_mode})")
            signals = cached_data["signals"]
            chunk_feats = cached_data["chunk_features"]
            duration = cached_data["duration"]
        else:
            print(f"Cache Miss for {file_hash[:8]}... (robustness_mode={robustness_mode}) Extracting features.")
            # Open file
            with open(filepath, 'rb') as f:
                wav_bytes = f.read()
                wav_io = io.BytesIO(wav_bytes)

            if robustness_mode:
                wav_io = audio_utils.apply_noise(wav_io)

            signals, y, sr = feature_extraction.extract_features(wav_io)
            duration = len(y) / sr
            
            # Chunk Analysis - extract features for chunks
            chunk_feats = feature_extraction.extract_chunk_features(y, sr)

            # Store in Cache
            FEATURE_CACHE[cache_key] = {
                "signals": signals,
                "chunk_features": chunk_feats,
                "duration": duration
            }
        
        # Chunk Analysis - aggregate scores
        chunk_analysis = detector.aggregate_chunk_scores(chunk_feats)
        
        # Inject chunk stability into signals for AI Detection Model
        # passing as specific key 'chunk_std' (using stability score as proxy for now)
        signals["chunk_std"] = chunk_analysis.get("stability_score", 0)

        # Detection (Now uses ML Model or Advanced Heuristic)
        detection_result = detector.detect_ai(signals)
        
        # Warnings
        warnings = detector.generate_warnings(signals, duration)

        # Construct Response
        final_confidence = detection_result["confidence"] # Float 0.0-1.0
        
        result = {
            "status": "success", # Legacy
            "assessment": detection_result["classification"], # New
            "risk_level": "High" if final_confidence > 0.75 else "Low", 
            "confidence": final_confidence, # Float
            "top_signals": detection_result["explanation"][:3], # New
            
            "chunk_confidence": chunk_analysis.get("chunk_confidence", []), # New
            
            # Existing Fields (Extended)
            "evidence_score": {
                **detection_result["score_breakdown"],
                "chunk_stability": chunk_analysis.get("stability_score", 0),
                "robustness": 4 if robustness_mode else 0
            },
            "explanation": detection_result["explanation"],
            "warnings": warnings,
            "signals": signals,
            "chunk_analysis": chunk_analysis,
            "robustness_applied": robustness_mode,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        return jsonify(result), 200

    return jsonify({'error': 'Unknown error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
