from flask import Flask
from dotenv import load_dotenv
import os

from routes import voice_detection_bp
from model.model_loader import load_model_and_scaler

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["API_KEY"] = os.getenv("API_KEY")
    if not app.config["API_KEY"]:
        raise RuntimeError("API_KEY is missing in environment variables")
    load_model_and_scaler()
    app.register_blueprint(voice_detection_bp, url_prefix="/api")
    return app
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
