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
                "confidence": round(0.95 + (random.random() * 0.04), 2),
                "tone": "Aggressive / Urgent",
                "keywords": ["verify", "immediate action", "block", "otp"]
            }
        elif rand_val > 0.4:
            result = {
                "status": "spam",
                "confidence": round(0.85 + (random.random() * 0.10), 2),
                "tone": "Persuasive / Sales",
                "keywords": ["offer", "lifetime free", "credit card", "limited period"]
            }
        else:
            result = {
                "status": "safe",
                "confidence": round(0.90 + (random.random() * 0.09), 2),
                "tone": "Neutral / Casual",
                "keywords": []
            }

        return jsonify(result), 200

    return jsonify({'error': 'Unknown error'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
