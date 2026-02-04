def build_explanation(features, quality_factor):
    """
    Build detailed, human-readable explanation of voice analysis
    Features are passed as a list in order:
    [pitch_mean, pitch_var, pitch_range, flatness_mean, centroid_mean, zcr_mean, ...]
    """
    # Extract features from list
    pitch_mean = features[0] if len(features) > 0 else 0
    pitch_var = features[1] if len(features) > 1 else 0
    pitch_range = features[2] if len(features) > 2 else 0
    flatness_mean = features[3] if len(features) > 3 else 0
    centroid_mean = features[4] if len(features) > 4 else 0
    zcr_mean = features[5] if len(features) > 5 else 0
    
    explanation_parts = []
    
    # 1. Pitch Analysis
    if pitch_var < 35:
        explanation_parts.append(
            f"🎵 Pitch Analysis: The voice exhibits extremely high pitch stability (variance: {pitch_var:.1f}). "
            "This lack of natural jitter is a strong characteristic of synthetic or AI-generated speech."
        )
    elif pitch_var > 120:
        explanation_parts.append(
            f"🎵 Pitch Analysis: Strong natural pitch variations detected (variance: {pitch_var:.1f}). "
            "This complex, organic fluctuation is a primary indicator of biological human speech."
        )
    else:
        explanation_parts.append(
            f"🎵 Pitch Analysis: Normal pitch variation observed (variance: {pitch_var:.1f}). "
            "The fluctuations fall within the expected range for human speech patterns."
        )
    
    # 2. Pitch Range Analysis
    if pitch_range < 120:
        explanation_parts.append(
            f"📊 Dynamic Range: Detected a very narrow pitch range of {pitch_range:.0f} Hz. "
            "While biological voices can be monotone, this restricted range is common in base-level synthetic voices."
        )
    elif pitch_range > 300:
        explanation_parts.append(
            f"📊 Dynamic Range: Wide dynamic range observed ({pitch_range:.0f} Hz). "
            "This emotional depth and emphasis variation are highly characteristic of natural human speakers."
        )
    else:
        explanation_parts.append(
            f"📊 Dynamic Range: Moderate dynamic range detected ({pitch_range:.0f} Hz), "
            "typical of conversational human speech."
        )
    
    # 3. Spectral Texture
    if flatness_mean < 0.22:
        explanation_parts.append(
            f"🎼 Spectral Texture: Low spectral complexity ({flatness_mean:.3f}). "
            "Synthetic voices often produce highly 'clean' spectral signatures compared to organic human voice."
        )
    elif flatness_mean > 0.45:
        explanation_parts.append(
            f"🎼 Spectral Texture: High spectral complexity ({flatness_mean:.3f}), "
            "capturing the natural 'breathiness' and environmental artifacts typical of human recordings."
        )
    else:
        explanation_parts.append(
            f"🎼 Spectral Texture: Standard spectral characteristics observed ({flatness_mean:.3f})."
        )
    
    # 4. Technical Summary
    details = []
    if pitch_mean > 0: details.append(f"Base pitch: {pitch_mean:.1f} Hz")
    if centroid_mean > 0: details.append(f"Spectral centroid: {centroid_mean:.0f} Hz")
    if zcr_mean > 0: details.append(f"ZCR: {zcr_mean:.4f}")
    
    if details:
        explanation_parts.append(f"📈 Metrics: {', '.join(details)}.")
    
    # 5. Quality Impact
    if quality_factor < 0.8:
        explanation_parts.append(
            f"⚠️ Note: Audio quality is suboptimal ({quality_factor:.2f}), "
            "which may slightly reduce detection confidence."
        )
    
    # 6. Conclusion
    explanation_parts.append(
        "💡 The final determination is based on a hybrid analysis of deep learning patterns "
        "and acoustic biological markers (jitter, shimmer, and spectral complexity)."
    )
    
    return " ".join(explanation_parts)
