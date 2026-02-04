function ErrorAlert({ message }) {
    return (
        <div className="error">
            <div style={{ fontSize: "1.5rem", marginBottom: "0.5rem" }}>⚠️</div>
            <strong>Error:</strong> {message}
        </div>
    );
}

export default ErrorAlert;
