function AnalyzeButton({ disabled, loading, onClick }) {
    return (
        <button className="button" disabled={disabled} onClick={onClick}>
            {loading ? "Analyzing..." : "Analyze Voice"}
        </button>
    );
}

export default AnalyzeButton;
