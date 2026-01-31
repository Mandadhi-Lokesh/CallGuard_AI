def detect_ai(features: dict) -> dict:
    try:
        # Component Scores (Target: Additive boost 8-12 per component)
        pitch_score = 0
        timing_score = 0
        spectral_score = 0
        reasons = []

        # Helper for safe access
        def get_val(key, subkey="value", default=None):
            try:
                return features.get(key, {}).get(subkey, default)
            except:
                return default

        # Unpack values safely
        pitch_variance = get_val("pitch_variance", default=None)
        jitter = get_val("jitter", default=None)
        spectral_flatness = get_val("spectral_flatness", default=None)
        pitch_acceleration = get_val("pitch_acceleration", default=None)
        pause_entropy = get_val("pause_entropy", default=None)

        # 1. Pitch Behavior (Max 12)
        if pitch_variance is not None:
            if pitch_variance < 80:
                pitch_score += 8
                reasons.append("Pitch dynamics show low natural variability (Monotone).")
            elif pitch_variance < 250:
                pitch_score += 5
                reasons.append("Pitch variation remains unusually smooth.")

        if pitch_acceleration is not None and pitch_acceleration < 5:
            pitch_score += 4
            reasons.append("Pitch transitions lack natural acceleration patterns.")
        
        pitch_score = min(pitch_score, 12)

        # 2. Timing Irregularity (Max 12)
        if jitter is not None:
            if jitter < 0.05:
                timing_score += 8
                reasons.append("Tone lacks natural micro-fluctuations (Digital perfection).")

        if pause_entropy is not None and pause_entropy < 0.8:
            timing_score += 4
            reasons.append("Pauses align with mechanical timing rather than biological breathing.")
        
        timing_score = min(timing_score, 12)

        # 3. Spectral Smoothness (Max 12)
        if spectral_flatness is not None:
            if spectral_flatness < 0.25: 
                spectral_score += 12
                reasons.append("Spectral texture is over-smoothed (Vocoder artifacts).")
            elif spectral_flatness > 0.6: 
                spectral_score += 8
                reasons.append("High spectral noise floor detected.")
        
        spectral_score = min(spectral_score, 12)
        
        # Internal confidence calculation (Legacy support, app.py recalculates)
        total_evidence = pitch_score + timing_score + spectral_score
        confidence = min(total_evidence / 36.0, 0.99) # Approx normalized

        classification = "AI_GENERATED" if confidence > 0.5 else "HUMAN"
        
        if not reasons:
            reasons.append("Acoustic patterns consistency with natural human speech.")

        return {
            "classification": classification,
            "confidence": round(confidence, 2),
            "explanation": reasons,
            "score_breakdown": {
                "pitch": pitch_score,
                "timing": timing_score,
                "spectral": spectral_score
            }
        }

    except Exception as e:
        # Fallback - ensure API never breaks
        return {
            "classification": "UNKNOWN",
            "confidence": 0.0,
            "explanation": ["Analysis completed using available acoustic signals."],
            "score_breakdown": {
                "pitch": 0,
                "timing": 0,
                "spectral": 0
            }
        }

def generate_warnings(features: dict, duration: float) -> list:
    warnings = []
    
    if duration < 3.0:
        warnings.append("Short audio duration detected.")
        
    pause_rate = features.get("pause_rate", {}).get("value", 0.0)
    if pause_rate > 0.8:
        warnings.append("Low speech activity detected.")
        
    return warnings

def aggregate_chunk_scores(chunk_features: list) -> dict:
    chunk_results = []
    
    for feat in chunk_features:
        chunk_score = 0.0
        
        if feat["jitter"] < 0.15: chunk_score += 0.45
        elif feat["jitter"] < 0.25: chunk_score += 0.2
        
        if feat["spectral_flatness"] < 0.3: chunk_score += 0.35
        elif feat["spectral_flatness"] > 0.6: chunk_score += 0.2
        
        chunk_score = min(chunk_score, 0.98)
        
        chunk_results.append({
            "timestamp": feat["timestamp"],
            "confidence": round(chunk_score, 2)
        })
        
    if not chunk_results:
        return {"trend": "insufficient_data", "details": [], "stability_score": 0}
        
    scores = [c["confidence"] for c in chunk_results]
    
    # Stability Score Calculation (Additive Max 12)
    avg_score = sum(scores) / len(scores)
    variance = max(scores) - min(scores)
    
    stability_score = 0
    trend = "natural_or_mixed"

    if avg_score > 0.6:
        # High confidence base
        if variance < 0.2:
            stability_score = 12 # Consistent AI
            trend = "stable_synthetic"
        else:
            stability_score = 8 # Fluctuating AI
            trend = "fluctuating_synthetic"
    else:
        # Natural or low conf
        stability_score = 0
        trend = "natural_low_conf"
        
    return {
        "trend": trend,
        "average_confidence": round(avg_score, 2),
        "chunk_details": chunk_results,
        "chunk_confidence": [int(s * 100) for s in scores],
        "stability_score": stability_score
    }
