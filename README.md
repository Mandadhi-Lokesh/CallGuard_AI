# CallGuard AI - Intelligent Call Fraud Detection

> **Protecting India's digital ecosystem from voice phishing and scam calls.**

## Problem Statement
Voice phishing (vishing) and spam calls are a massive issue in India, costing millions in financial losses annually. Vulnerable populations, especially senior citizens, are often targeted by sophisticated social engineering attacks that traditional blocklists cannot detect.

## Solution
**CallGuard AI** is a pro-active audio analysis system that detects fraud *content* and *intent*, not just blacklisted numbers. By analyzing speech patterns, urgency, and specific keywords, it provides a real-time risk assessment of recorded calls.

## Architecture
The application follows a clean, decoupled architecture:
- **Frontend**: React (Vite) + Tailwind CSS (Dark Mode) + Framer Motion.
    - Focuses on a premium, trustworthy user interface.
- **Backend**: Python Flask REST API.
    - Handles audio processing and ML inference simulation.
    - Returns JSON responses with transparent confidence scores and explainability factors.

## Technology Stack
- **Frontend**: React, React Router, Lucide Icons, Axios/Fetch.
- **Backend**: Flask, Flask-CORS, Python.
- **Design**: "Cyber-Security" Dark Blue Theme, Glassmorphism.

## Demo Instructions
1. **Clone the repository**.
2. **Start the Backend**:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   *Server runs on http://localhost:5000*

3. **Start the Frontend**:
   ```bash
   npm install
   npm run dev
   ```
   *Open http://localhost:5173*

4. **Test the Flow**:
   - Navigate to **Analyzer**.
   - Upload an audio file (.wav/.mp3).
   - View the detailed **Result** with explainability metrics.

---
*Disclaimer: This is a prototype system developed for educational and hackathon demonstration purposes. The analysis data is simulated.*
