function ResultCard({ result }) {
    const isAI = result.classification === "AI_GENERATED";
    const confidence = (result.confidenceScore * 100).toFixed(1);
    const isMultilingual = result.isMultilingual || false;
    const detectedLanguages = result.allDetectedLanguages || result.detectedLanguages || [result.language];

    const languageConfidence = result.languageConfidence
        ? (result.languageConfidence * 100).toFixed(0)
        : null;

    return (
        <div className="result-card">
            <div style={{ textAlign: "center", marginBottom: "1.5rem" }}>
                <div style={{ fontSize: "4rem", marginBottom: "1rem" }}>
                    {isAI ? "🤖" : "👤"}
                </div>
                <h2 style={{
                    color: isAI ? "var(--danger)" : "var(--secondary)",
                    marginBottom: "0.5rem"
                }}>
                    {isAI ? "AI Generated" : "Human Voice"}
                </h2>
            </div>

            {/* Language Detection Info */}
            <div style={{
                padding: "1rem",
                background: "var(--bg-secondary)",
                borderRadius: "var(--radius-md)",
                marginBottom: "1rem",
                borderLeft: "4px solid var(--primary)"
            }}>
                <div style={{ marginBottom: "0.5rem" }}>
                    <strong>🌐 Detected Language{isMultilingual ? "s" : ""}:</strong>
                    {isMultilingual && (
                        <span style={{
                            marginLeft: "0.5rem",
                            padding: "0.2rem 0.5rem",
                            background: "rgba(139, 92, 246, 0.2)",
                            borderRadius: "0.25rem",
                            fontSize: "0.75rem",
                            color: "#c084fc"
                        }}>
                            MULTILINGUAL
                        </span>
                    )}
                </div>
                <div style={{ fontSize: "1.1rem", color: "var(--primary-light)" }}>
                    {detectedLanguages.join(" + ")}
                </div>
                {languageConfidence && (
                    <div style={{ fontSize: "0.85rem", color: "var(--text-muted)", marginTop: "0.25rem" }}>
                        Confidence: {languageConfidence}%
                    </div>
                )}
            </div>

            <div className="confidence-meter">
                <p style={{ marginBottom: "0.5rem" }}>
                    <strong>🎯 Classification Confidence:</strong> {confidence}%
                </p>
                <div className="confidence-bar">
                    <div
                        className="confidence-fill"
                        style={{
                            width: `${confidence}%`,
                            background: isAI
                                ? "linear-gradient(90deg, #ef4444 0%, #dc2626 100%)"
                                : "linear-gradient(90deg, #10b981 0%, #059669 100%)"
                        }}
                    />
                </div>
            </div>

            <div style={{
                marginTop: "1.5rem",
                padding: "1rem",
                background: "var(--bg-secondary)",
                borderRadius: "var(--radius-md)",
                borderLeft: `4px solid ${isAI ? "var(--danger)" : "var(--secondary)"}`
            }}>
                <p style={{ fontSize: "0.95rem", lineHeight: "1.8" }}>
                    <strong style={{ display: "block", marginBottom: "0.5rem" }}>
                        📊 Analysis:
                    </strong>
                    {result.explanation}
                </p>
            </div>
        </div>
    );
}

export default ResultCard;
