import librosa
import numpy as np
from scipy.stats import variation

def get_interpretation(value, low_thresh, high_thresh, inverse=False):
    if inverse:
        if value < low_thresh: return "High"
        if value < high_thresh: return "Medium"
        return "Low"
    else:
        if value < low_thresh: return "Low"
        if value < high_thresh: return "Medium"
        return "High"

def extract_features(wav_io):
    y, sr = librosa.load(wav_io, sr=16000)
    
    signals = {}

    # 1. Pitch Extraction (Vectorized & Safe)
    try:
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        # Vectorized implementation
        indices = magnitudes.argmax(axis=0)
        t_steps = np.arange(pitches.shape[1])
        pitch_values = pitches[indices, t_steps]
        pitch_values = pitch_values[pitch_values > 0] # Filter silence/zeros
        
        if len(pitch_values) > 1:
            pitch_variance = float(np.var(pitch_values))
            jitter = float(variation(pitch_values)) if np.mean(pitch_values) > 0 else 0.0
            pitch_derivative = np.diff(pitch_values)
            pitch_acceleration = float(np.mean(np.abs(pitch_derivative)))
        else:
            pitch_variance = 0.0
            jitter = 0.0
            pitch_acceleration = 0.0
            
        signals["pitch_variance"] = {
             "value": pitch_variance, "interpretation": get_interpretation(pitch_variance, 100, 500)
        }
        signals["jitter"] = {
             "value": jitter, "interpretation": get_interpretation(jitter, 0.05, 0.2)
        }
        signals["pitch_acceleration"] = {
             "value": pitch_acceleration, "interpretation": get_interpretation(pitch_acceleration, 5, 20)
        }
    except Exception as e:
        print(f"Pitch extraction failed: {e}")
        # Default safe values
        signals["pitch_variance"] = {"value": 0.0, "interpretation": "Low"}
        signals["jitter"] = {"value": 0.0, "interpretation": "Low"}
        signals["pitch_acceleration"] = {"value": 0.0, "interpretation": "Low"}

    # 2. Energy (Safe)
    try:
        energy = librosa.feature.rms(y=y)[0]
        energy_variance = float(np.var(energy)) if len(energy) > 0 else 0.0
        # Energy isn't used in main scoring currently but good to have
    except:
        energy_variance = 0.0

    # 3. Pauses & Micro-Timing (Safe)
    try:
        intervals = librosa.effects.split(y, top_db=25)
        pauses = []
        if len(intervals) > 1:
            # Vectorize pause calculation? Iteration is fast enough for intervals (usually few)
            for i in range(1, len(intervals)):
                pause_duration = (intervals[i][0] - intervals[i - 1][1]) / sr
                if pause_duration > 0.05:
                    pauses.append(pause_duration)
        
        pause_rate = len(pauses) / (len(y) / sr) if len(y) > 0 else 0.0
        
        if len(pauses) > 1:
            hist, _ = np.histogram(pauses, bins=5, density=True)
            pause_entropy = float(scipy.stats.entropy(hist + 1e-10))
            pause_irregularity = float(np.std(pauses) / (np.mean(pauses) + 1e-5))
        else:
            pause_entropy = 0.0
            pause_irregularity = 0.0
            
        signals["pause_rate"] = {
            "value": pause_rate, "interpretation": get_interpretation(pause_rate, 0.2, 0.8, inverse=True)
        }
        signals["pause_entropy"] = {
            "value": pause_entropy, "interpretation": get_interpretation(pause_entropy, 0.5, 1.5)
        }
        signals["pause_irregularity"] = {
            "value": pause_irregularity, "interpretation": get_interpretation(pause_irregularity, 0.2, 0.8)
        }
    except Exception as e:
        print(f"Pause extraction failed: {e}")
        signals["pause_rate"] = {"value": 0.0, "interpretation": "Low"}
        signals["pause_entropy"] = {"value": 0.0, "interpretation": "Low"}
        signals["pause_irregularity"] = {"value": 0.0, "interpretation": "Low"}

    # 4. Spectral (Safe)
    try:
        spectral_flatness = float(np.mean(librosa.feature.spectral_flatness(y=y)))
        centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        harmonic_consistency = 1.0 / (float(np.var(centroids)) + 1e-5)
        
        signals["spectral_flatness"] = {
            "value": spectral_flatness, "interpretation": get_interpretation(spectral_flatness, 0.01, 0.2, inverse=True)
        }
        signals["harmonic_consistency"] = {
            "value": harmonic_consistency, "interpretation": "High" if harmonic_consistency > 0.0001 else "Low"
        }
    except Exception as e:
        print(f"Spectral extraction failed: {e}")
        signals["spectral_flatness"] = {"value": 0.0, "interpretation": "Low"}
        signals["harmonic_consistency"] = {"value": 0.0, "interpretation": "Low"}

    return signals, y, sr

def extract_chunk_features(y, sr, chunk_duration=1.5):
    chunk_samples = int(chunk_duration * sr)
    total_samples = len(y)
    chunks_features = []
    
    for start in range(0, total_samples, chunk_samples):
        end = min(start + chunk_samples, total_samples)
        if (end - start) < sr * 0.5: continue
            
        y_chunk = y[start:end]
        spectral_flatness = float(np.mean(librosa.feature.spectral_flatness(y=y_chunk)))
        
        pitches, mags = librosa.piptrack(y=y_chunk, sr=sr)
        pitch_vals = pitches[mags > np.median(mags)]
        pitch_vals = pitch_vals[pitch_vals > 0]
        
        if len(pitch_vals) > 10:
            jitter = float(variation(pitch_vals))
            pitch_variance = float(np.var(pitch_vals))
        else:
            jitter = 0.0
            pitch_variance = 0.0
        
        chunks_features.append({
            "spectral_flatness": spectral_flatness,
            "jitter": jitter,
            "pitch_variance": pitch_variance,
            "timestamp": start / sr
        })
        
    return chunks_features
