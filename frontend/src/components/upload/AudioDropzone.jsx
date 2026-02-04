import { useState, useRef } from "react";

function AudioDropzone({ onFileSelect }) {
    const [isDragging, setIsDragging] = useState(false);
    const [fileName, setFileName] = useState("");
    const fileInputRef = useRef(null);

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            if (file.type === "audio/mpeg" || file.name.toLowerCase().endsWith('.mp3')) {
                setFileName(file.name);
                onFileSelect(file);
            } else {
                alert("Only MP3 files are accepted.");
            }
        }
        if (fileInputRef.current) {
            fileInputRef.current.value = "";
        }
    };

    const handleDragOver = (e) => {
        e.preventDefault();
        setIsDragging(true);
    };

    const handleDragLeave = () => {
        setIsDragging(false);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setIsDragging(false);
        const file = e.dataTransfer.files[0];
        if (file) {
            if (file.type === "audio/mpeg" || file.name.toLowerCase().endsWith('.mp3')) {
                setFileName(file.name);
                onFileSelect(file);
            } else {
                alert("Only MP3 files are accepted.");
            }
        }
    };

    const handleClick = () => {
        if (fileInputRef.current) {
            fileInputRef.current.click();
        }
    };

    return (
        <div
            className={`dropzone ${isDragging ? "dragging" : ""}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={handleClick}
            style={{ cursor: "pointer" }}
        >
            <div style={{ fontSize: "3rem", marginBottom: "1rem" }}>🎵</div>
            <input
                type="file"
                accept=".mp3,audio/mpeg"
                onChange={handleFileChange}
                ref={fileInputRef}
                style={{ display: "none" }}
            />
            <div>
                {fileName ? (
                    <div>
                        <p style={{ color: "var(--primary-light)", fontWeight: 600 }}>
                            ✓ {fileName}
                        </p>
                        <p style={{ fontSize: "0.9rem", marginTop: "0.5rem", color: "var(--text-secondary)" }}>
                            Click to change MP3 file
                        </p>
                    </div>
                ) : (
                    <div>
                        <p style={{ fontSize: "1.1rem", fontWeight: 600, marginBottom: "0.5rem" }}>
                            Upload MP3 Audio File
                        </p>
                        <p style={{ fontSize: "0.9rem", color: "var(--text-secondary)" }}>
                            Drag and drop or click anywhere to browse
                        </p>
                    </div>
                )}
            </div>
        </div>
    );
}

export default AudioDropzone;
