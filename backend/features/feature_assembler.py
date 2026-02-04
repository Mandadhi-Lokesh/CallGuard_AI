from features.pitch_features import extract_pitch_features
from features.spectral_features import extract_spectral_features
from features.mfcc_features import extract_mfcc_features

def extract_all_features(y, sr):
    features = []
    features.extend(extract_pitch_features(y, sr))
    features.extend(extract_spectral_features(y, sr))
    features.extend(extract_mfcc_features(y, sr))
    return features
