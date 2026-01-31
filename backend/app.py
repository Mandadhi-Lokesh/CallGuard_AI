from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

        # Open file
        with open(filepath, 'rb') as f:
            wav_bytes = f.read()
            wav_io = io.BytesIO(wav_bytes)

        if robustness_mode:
            wav_io = audio_utils.apply_noise(wav_io)

        signals, y, sr = feature_extraction.extract_features(wav_io)
        duration = len(y) / sr
        
        # Detection
        detection_result = detector.detect_ai(signals)
        
        # Chunk Analysis
        chunk_feats = feature_extraction.extract_chunk_features(y, sr)
        chunk_analysis = detector.aggregate_chunk_scores(chunk_feats)
        
        # Warnings
        warnings = detector.generate_warnings(signals, duration)

        # Aggregated Evidence Score Calculation
        score_breakdown = detection_result.get("score_breakdown", {"pitch":0,"timing":0,"spectral":0})
        robustness_score = 4 if robustness_mode else 0

        # New Additive Confidence Logic (Base 55)
        base_confidence = 55
        
        additive_boost = (
            score_breakdown.get("pitch", 0) + 
            score_breakdown.get("timing", 0) + 
            score_breakdown.get("spectral", 0) + 
            chunk_analysis.get("stability_score", 0) + 
            robustness_score
        )
        
        total_score = base_confidence + additive_boost
        final_confidence = min(total_score, 90) / 100.0
        
        # Determine Label 
        # > 75% -> Synthetic Voice Signature (High)
        # 55-75% -> Mixed Acoustic Signals (Medium)
        
        if final_confidence > 0.75:
            display_status = "fraud"
            risk_level = "High"
        elif final_confidence >= 0.55:
            display_status = "spam"
            risk_level = "Medium"
        else:
            display_status = "safe"
            risk_level = "Low"
            
        # Overrule if absolutely no evidence found
        if additive_boost < 4:
             display_status = "safe"
             risk_level = "Low"

        # Construct Response
        result = {
            "status": display_status,
            "risk_level": risk_level,
            "confidence": round(final_confidence, 2),
            "evidence_score": {
                "pitch": score_breakdown.get("pitch", 0),
                "timing": score_breakdown.get("timing", 0),
                "spectral": score_breakdown.get("spectral", 0),
                "chunk_stability": chunk_analysis.get("stability_score", 0),
                "robustness": robustness_score
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
