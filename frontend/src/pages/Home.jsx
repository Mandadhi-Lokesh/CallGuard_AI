import { useState } from "react";
import AudioDropzone from "../components/upload/AudioDropzone";
import AnalyzeButton from "../components/controls/AnalyzeButton";
import ResultCard from "../components/results/ResultCard";
import JsonViewer from "../components/results/JsonViewer";
import ErrorAlert from "../components/feedback/ErrorAlert";
import { analyzeVoice } from "../services/voiceApi";
import { fileToBase64 } from "../utils/base64";

function Home() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState(null);
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    const handleFileSelect = (selectedFile) => {
        setFile(selectedFile);
        setResult(null);
        setError("");
    };

    const handleAnalyze = async () => {
        if (!file) {
            setError("Please upload an MP3 audio file first");
            return;
        }

        try {
            setLoading(true);
            setError("");
            setResult(null);

            const base64Audio = await fileToBase64(file);
            const format = file.name?.split('.').pop().toLowerCase();

            if (format !== "mp3") {
                throw new Error("Only MP3 files are supported");
            }

            const payload = {
                audioFormat: "mp3",
                audioBase64: base64Audio,
            };

            const response = await analyzeVoice(payload);
            setResult(response);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <main className="container">
            <h1>AI-Generated Voice Detection</h1>
            <p className="subtitle">
                Upload an MP3 audio file to detect AI-generated voices. Language will be auto-detected.
            </p>

            <AudioDropzone onFileSelect={handleFileSelect} />

            <div style={{ marginTop: "2rem", display: "flex", justifyContent: "center" }}>
                <AnalyzeButton
                    disabled={!file || loading}
                    loading={loading}
                    onClick={handleAnalyze}
                />
            </div>

            {error && <ErrorAlert message={error} />}
            {result && (
                <div style={{ animation: "fadeIn 0.5s ease-out" }}>
                    <ResultCard result={result} />
                    <JsonViewer data={result} />
                </div>
            )}
        </main>
    );
}

export default Home;
