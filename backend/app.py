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
        
        # Simulate processing time
        time.sleep(2)
        
        # Mock ML Inference Logic
        # In a real app, this would be: model.predict(filepath)
        
        # Deterministic but seemingly random logic based on filename length
        # to ensure the same file gets the same result during demo
        seed = len(file.filename)
        random.seed(seed)
        
        rand_val = random.random()
        
        if rand_val > 0.7:
            result = {
                "status": "fraud",
                "risk_level": "High",
                "confidence": round(0.87 + (random.random() * 0.12), 2),
                "tone": "Aggressive / Urgent",
                "keywords": ["verify", "immediate action", "block", "otp"],
                "explanation": [
                    "Detected high-urgency phrases demanding immediate action.",
                    "Frequent use of banking-related keywords (OTP, Block).",
                    "Abnormal speech cadence indicating scripted threats."
                ]
            }
        elif rand_val > 0.4:
            result = {
                "status": "spam",
                "risk_level": "Medium",
                "confidence": round(0.75 + (random.random() * 0.10), 2),
                "tone": "Persuasive / Sales",
                "keywords": ["offer", "lifetime free", "credit card", "limited period"],
                "explanation": [
                    "Detected repetitive sales pitch patterns.",
                    "Unsolicited offer keywords identified.",
                    "Tone analysis suggests persuasive telemarketing."
                ]
            }
        else:
            result = {
                "status": "safe",
                "risk_level": "Low",
                "confidence": round(0.92 + (random.random() * 0.07), 2),
                "tone": "Neutral / Casual",
                "keywords": [],
                "explanation": [
                    "No malicious patterns detected.",
                    "Natural conversation flow.",
                    "No known fraud keywords found."
                ]
            }

        result["model_version"] = "v1.0 (Demo)"
        result["processing_note"] = "Audio analyzed securely on server"
        result["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

        return jsonify(result), 200

    return jsonify({'error': 'Unknown error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
