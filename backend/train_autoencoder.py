"""
ONE-CLASS AUTOENCODER TRAINING SCRIPT (Offline)
Author: Expert AI Architect
Description: Trains a reconstruction model using ONLY AI-generated audio samples.
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import joblib
import os

# Configuration
INPUT_DIM = 50 # 5 Pitch + 6 Spectral + 39 MFCC
LATENT_DIM = 8 # Compressed representation
EPOCHS = 100
BATCH_SIZE = 16

def build_autoencoder(input_dim, latent_dim):
    # Encoder
    inputs = layers.Input(shape=(input_dim,))
    encoder = layers.Dense(32, activation='relu')(inputs)
    encoder = layers.Dense(16, activation='relu')(encoder)
    latent = layers.Dense(latent_dim, activation='relu')(encoder)
    
    # Decoder
    decoder = layers.Dense(16, activation='relu')(latent)
    decoder = layers.Dense(32, activation='relu')(decoder)
    outputs = layers.Dense(input_dim, activation='linear')(decoder)
    
    autoencoder = models.Model(inputs, outputs)
    autoencoder.compile(optimizer='adam', loss='mse')
    return autoencoder

def train_one_class_model(ai_features_path):
    """
    Args:
        ai_features_path: Path to .npy file containing AI feature vectors (N, 50)
    """
    if not os.path.exists(ai_features_path):
        print("❌ Error: AI Training features not found. Please run feature extraction first.")
        return

    # Load AI-only data
    X_train = np.load(ai_features_path)
    
    # Scale Data
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    # Build and Train
    ae = build_autoencoder(INPUT_DIM, LATENT_DIM)
    print("🚀 Training One-Class Autoencoder on AI samples...")
    ae.fit(X_train_scaled, X_train_scaled, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1, verbose=1)
    
    # Calculate Reconstruction Threshold T
    # T = 95th percentile of training MSE
    X_pred = ae.predict(X_train_scaled)
    mse = np.mean(np.square(X_train_scaled - X_pred), axis=1)
    threshold_t = np.percentile(mse, 95)
    
    print(f"✅ Training Complete. Recommended Threshold T: {threshold_t:.4f}")
    
    # Save Assets
    os.makedirs('assets', exist_ok=True)
    ae.save('assets/model.h5')
    joblib.dump(scaler, 'assets/scaler.pkl')
    print("📁 Assets saved to backend/assets/")

if __name__ == "__main__":
    # Example usage (requires pre-extracted ai_features.npy)
    # train_one_class_model('data/ai_features.npy')
    print("Ready for offline training. Provide AI-only feature vector path.")
