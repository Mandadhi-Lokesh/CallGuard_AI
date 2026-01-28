# CallGuard AI - India AI Impact Buildathon
### 🛡️ AI-Powered Call Fraud Detection System

**Team: CyberSentinels**  
**Track: AI for Security**

> **Problem Statement**  
> India loses crores daily to voice phishing (vishing) and financial fraud calls. Senior citizens and non-tech-savvy users are particularly vulnerable to high-pressure tactics. Traditional blocklists fail against new numbers and VoIP calls.

## 🚀 The Solution
**CallGuard AI** is an intelligent fraud detection system that analyzes the *content* and *intent* of a call, not just the phone number. 

Using advanced NLP patterns, it detects:
- **Urgency & Threats** ("Your account will be blocked", "Immediate payment")
- **Suspicious Keywords** ("OTP", "Refund", "KYC Update")
- **Socio-Linguistic Indicators** (Aggressive tone, repetitive persuation)

---

## 🏗️ Architecture
The system follows a decoupled, secure architecture designed for scalability.

```
[ Frontend: React + Tailwind ] 
       │ (Upload Audio)
       ▼
 [ Backend: Python Flask API ]
       │ (Feature Extraction)
       ▼
[ AI Logic / Inference Engine ]
       │ (Risk Classification)
       ▼
[ JSON Response: Label + Confidence + Explanation ]
```

## 🛠️ Technology Stack
- **Frontend**: React (Vite), Tailwind CSS (Dark Theme), Framer Motion
- **Backend**: Python, Flask, Flask-CORS
- **Design**: "Cyber-Trust" aesthetic, dark mode optimized, mobile-responsive.

---

## ⚡ How to Run Locally

### 1. Clone & Setup Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```
*Server runs on port 5000*

### 2. Setup Frontend
```bash
# In a new terminal
npm install
npm run dev
```
*Open http://localhost:5173*

## 📱 Demo Flow for Judges
1. **Analyze**: Go to the "Analyzer" tab.
2. **Upload**: Drop the provided sample audio file `scam_sample.mp3` (or any .wav).
3. **Wait**: Observe the "Analyzing" state featuring secure processing.
4. **Result**: View the **High Risk** verdict, confidence score, and bullet-point explanation of *why* it was flagged.

---

*Disclaimer: This project is a prototype developed for the India AI Impact Buildathon. Analysis logic is simulated for demonstration purposes.*
