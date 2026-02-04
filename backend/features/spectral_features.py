import numpy as np
import librosa

def extract_spectral_features(y, sr):
    flatness = librosa.feature.spectral_flatness(y=y)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)

    return [
        float(np.mean(flatness)),
        float(np.mean(centroid)),
        float(np.mean(zcr))
    ]
