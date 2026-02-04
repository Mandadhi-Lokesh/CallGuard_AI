import numpy as np
import librosa

def extract_pitch_features(y, sr):
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[pitches > 0]

    if len(pitch_values) == 0:
        return [0, 0, 0]

    return [
        float(np.mean(pitch_values)),
        float(np.var(pitch_values)),
        float(np.max(pitch_values) - np.min(pitch_values))
    ]
