import { API_BASE_URL, API_KEY } from "../config";

export async function analyzeVoice(payload) {
    const response = await fetch(`${API_BASE_URL}/voice-detection`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "x-api-key": API_KEY,
        },
        body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (!response.ok) {
        throw new Error(data.message || "Request failed");
    }

    return data;
}
