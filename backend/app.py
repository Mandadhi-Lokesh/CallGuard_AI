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
                "risk_level": "Highest",
                "confidence": round(0.95 + (random.random() * 0.04), 2),
                "tone": "Aggressive / Urgent",
                "keywords": ["verify", "immediate action", "block", "otp"],
                "reasoning": "The caller used high-pressure tactics demanding immediate verification of personal banking details. Frequent use of 'block' and 'urgent' indicates a typical panic-inducing scam pattern."
            }
        elif rand_val > 0.4:
            result = {
                "status": "spam",
                "risk_level": "Medium",
                "confidence": round(0.85 + (random.random() * 0.10), 2),
                "tone": "Persuasive / Sales",
                "keywords": ["offer", "lifetime free", "credit card", "limited period"],
                "reasoning": "Call pattern matches telemarketing scripts. While likely not malicious, the unsolicited nature and repetitive sales keywords classify it as spam."
            }
        else:
            result = {
                "status": "safe",
                "risk_level": "Low",
                "confidence": round(0.90 + (random.random() * 0.09), 2),
                "tone": "Neutral / Casual",
                "keywords": [],
                "reasoning": "Natural conversation flow detected with no known threat indicators or suspicious keyword density."
            }

        result["model_version"] = "v2.1.0-alpha"
        result["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")

        return jsonify(result), 200

    return jsonify({'error': 'Unknown error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
