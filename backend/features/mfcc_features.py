import numpy as np
import librosa

def extract_mfcc_features(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    delta = librosa.feature.delta(mfcc)

    features = []
    features.extend(np.mean(mfcc, axis=1))
    features.extend(np.var(mfcc, axis=1))
    features.extend(np.var(delta, axis=1))

    return [float(x) for x in features]
