import librosa
import numpy as np

def extract_pitch_features(y, sr):
    pitches, _ = librosa.piptrack(y=y, sr=sr)
    pitch_values = pitches[pitches > 0]

    if len(pitch_values) == 0:
        return [0.0, 0.0, 0.0]

    return [
        float(np.mean(pitch_values)),
        float(np.var(pitch_values)),
        float(np.max(pitch_values) - np.min(pitch_values))
    ]


def extract_spectral_features(y, sr):
    flatness = librosa.feature.spectral_flatness(y=y)
    centroid = librosa.feature.spectral_centroid(y=y, sr=sr)

    return [
        float(np.mean(flatness)),
        float(np.var(flatness)),
        float(np.var(centroid))
    ]


def extract_mfcc_features(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)

    features = []
    features.extend(np.mean(mfcc, axis=1))
    features.extend(np.var(mfcc, axis=1))
    features.extend(np.var(delta, axis=1))

    return [float(x) for x in features]


def extract_all_features(file_path):
    y, sr = librosa.load(file_path, sr=None, mono=True)

    features = []
    features.extend(extract_pitch_features(y, sr))
    features.extend(extract_spectral_features(y, sr))
    features.extend(extract_mfcc_features(y, sr))

    return features
