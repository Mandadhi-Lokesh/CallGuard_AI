"""
Language Detection Module
Uses fuzzy acoustic logic to detect language(s) from audio features.
Restored for 45-feature format.
"""
import numpy as np

def get_membership(value, mean, std):
    if std == 0: return 1.0 if value == mean else 0.0
    z = (value - mean) / std
    return np.exp(-0.5 * (z**2))

def detect_language_from_audio(waveform, sr, features=None):
    languages = ['Tamil', 'English', 'Hindi', 'Malayalam', 'Telugu']
    lang_scores = {lang: 0.0 for lang in languages}
    
    if features and len(features) >= 45:
        pitch_mean = features[0]
        pitch_var = features[1]
        pitch_range = features[2]
        flatness_mean = features[3]
        centroid_mean = features[4]
        zcr_mean = features[5]
        mfcc_means = features[6:19]
        
        profiles = {
            'Tamil': {
                'pitch': (210, 30), 
                'centroid': (2800, 400),
                'flatness': (0.28, 0.1),
                'zcr': (0.07, 0.02)
            },
            'English': {
                'pitch': (145, 30), 
                'centroid': (2200, 500),
                'flatness': (0.45, 0.1),
                'zcr': (0.05, 0.02)
            },
            'Hindi': {
                'pitch': (185, 30), 
                'centroid': (2200, 300),
                'flatness': (0.35, 0.1),
                'zcr': (0.045, 0.02)
            },
            'Malayalam': {
                'pitch': (200, 30), 
                'centroid': (2400, 400),
                'flatness': (0.50, 0.1),
                'zcr': (0.06, 0.02)
            },
            'Telugu': {
                'pitch': (195, 35), 
                'centroid': (2350, 350),
                'flatness': (0.32, 0.1),
                'zcr': (0.05, 0.02)
            }
        }
        
        for lang, profile in profiles.items():
            p_score = get_membership(pitch_mean, profile['pitch'][0], profile['pitch'][1])
            c_score = get_membership(centroid_mean, profile['centroid'][0], profile['centroid'][1])
            f_score = get_membership(flatness_mean, profile['flatness'][0], profile['flatness'][1])
            z_score = get_membership(zcr_mean, profile['zcr'][0], profile['zcr'][1])
            
            total_score = (p_score * 0.4) + (c_score * 0.3) + (f_score * 0.2) + (z_score * 0.1)
            
            if lang == 'English' and mfcc_means[1] > -10: total_score += 0.1
            if lang == 'Tamil' and mfcc_means[2] < -15: total_score += 0.1
            if lang == 'Hindi' and -5 < mfcc_means[1] < 15: total_score += 0.1
            
            lang_scores[lang] = total_score
    else:
        return {
            "primary_language": "Unknown",
            "detected_languages": ["Unknown"],
            "is_multilingual": False,
            "confidence": 0.2
        }
    
    sorted_langs = sorted(lang_scores.items(), key=lambda x: x[1], reverse=True)
    primary_lang, primary_score = sorted_langs[0]
    
    if primary_score < 0.25:
        return {
            "primary_language": "Unknown",
            "detected_languages": ["Unknown"],
            "is_multilingual": False,
            "confidence": 0.1
        }
    
    detected_languages = [primary_lang]
    is_multilingual = False
    
    if len(sorted_langs) > 1:
        second_lang, second_score = sorted_langs[1]
        if second_score > 0.4 and (primary_score - second_score) < 0.15:
            detected_languages.append(second_lang)
            is_multilingual = True
            
    return {
        "primary_language": primary_lang,
        "detected_languages": detected_languages,
        "is_multilingual": is_multilingual,
        "confidence": float(round(min(primary_score * 1.5, 0.99), 2))
    }
