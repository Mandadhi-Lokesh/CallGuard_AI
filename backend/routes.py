from flask import Blueprint, request, jsonify, current_app

from utils.validators import validate_api_key, validate_request_json
from audio.base64_handler import decode_base64_audio
from audio.audio_decoder import decode_mp3
from features.feature_assembler import extract_all_features
from quality.quality_score import compute_quality_factor
from model.inference import run_inference, generate_one_class_explanation

voice_detection_bp = Blueprint("voice_detection", __name__)

@voice_detection_bp.route("/voice-detection", methods=["POST"])
def voice_detection():
    # 1. Security Check
    if not validate_api_key(request, current_app.config["API_KEY"]):
        return jsonify({"status": "error", "message": "Invalid API key"}), 401

    # 2. Payload Validation
    data = request.get_json(silent=True)
    error = validate_request_json(data)
    if error:
        return jsonify({"status": "error", "message": error}), 400

    try:
        # 3. Audio Decoding
        audio_bytes = decode_base64_audio(data["audioBase64"])
        waveform, sr = decode_mp3(audio_bytes)

        # 4. Feature Pipeline
        features = extract_all_features(waveform, sr)
        quality_factor = compute_quality_factor(waveform)

        # 5. One-Class Inference (Only AI known, Human is Anomaly)
        classification, confidence, mse_error = run_inference(features)
        
        # 6. Quality Adjustment
        # Low quality reduces confidence but classification remains fixed
        final_confidence = min(confidence, quality_factor) if quality_factor < 0.8 else confidence

        # 7. Explanation Logic
        explanation = generate_one_class_explanation(classification, features, mse_error)
        if quality_factor < 0.7:
            explanation += " (Confidence adjusted for low audio quality)"

        # 8. Success Response
        return jsonify({
            "status": "success",
            "language": data.get("language", "English"),
            "classification": classification,
            "confidenceScore": round(final_confidence, 3),
            "explanation": explanation
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)}), 500
