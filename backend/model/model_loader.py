import joblib
import tensorflow as tf
import os

MODEL = None
SCALER = None

def load_model_and_scaler():
    global MODEL, SCALER
    # Use absolute paths to avoid issues with CWD
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "assets", "model.h5")
    scaler_path = os.path.join(base_dir, "assets", "scaler.pkl")
    
    try:
        if os.path.exists(model_path) and os.path.exists(scaler_path):
            MODEL = tf.keras.models.load_model(model_path)
            SCALER = joblib.load(scaler_path)
            print(f"✅ Model and Scaler loaded successfully from {base_dir}")
        else:
            print(f"❌ Assets not found at {model_path} or {scaler_path}")
    except Exception as e:
        print(f"⚠️ WARNING: Could not load model/scaler ({e}). Running in MOCK mode.")
        MODEL = None
        SCALER = None
