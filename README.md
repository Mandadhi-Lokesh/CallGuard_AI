# CallGuard AI - India AI Impact Buildathon
### 🛡️ AI-Powered Call Fraud Detection System

**Team: CyberSentinels**  
**Track: AI for Security**

> **Problem Statement**  
> India loses crores daily to voice phishing (vishing) and financial fraud calls. Senior citizens and non-tech-savvy users are particularly vulnerable to high-pressure tactics. Traditional blocklists fail against new numbers and VoIP calls.

## 🚀 Proposed Solution
**CallGuard AI** is an intelligent fraud detection system that analyzes the *content* and *intent* of a call, not just the phone number. 

Using advanced NLP patterns, it detects:
- **Urgency & Threats** ("Your account will be blocked", "Immediate payment")
- **Suspicious Keywords** ("OTP", "Refund", "KYC Update")
- **Socio-Linguistic Indicators** (Aggressive tone, repetitive persuasion)

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

## 🧠 AI Detection Logic (High-Level)
The system currently uses a rule-based and pattern-driven inference approach designed to approximate real-world AI decision-making behavior:
- Keyword and phrase risk scoring
- Urgency and threat detection
- Aggregated confidence calculation
- Risk categorization (High / Medium / Low)

This design allows easy replacement with ML/DL models in future iterations.

## 🛠️ Technology Stack
- **Frontend**: React (Vite), Tailwind CSS (Dark Theme)
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

## 🌐 Live Deployment
Frontend and backend are deployed and publicly accessible:

- **Live URL**: <PASTE YOUR DEPLOYED LINK HERE>

The application is optimized for both desktop and mobile browsers.

## 📱 Demo Flow for Judges
1. Navigate to the **Analyzer** tab.
2. Upload a call audio file (.mp3 or .wav).
3. Observe the secure **Analyzing** state.
4. View the risk verdict, confidence score, and explanation.
5. (Optional) Upload an unsupported file to see graceful error handling.

## 🇮🇳 Impact & Use Cases
- Protecting senior citizens from voice phishing
- Assisting telecom providers with fraud screening
- Raising awareness about scam call patterns
- Foundation for real-time call monitoring systems

## 🔮 Future Scope
- Integration with real-time call streams
- Multilingual scam detection (regional Indian languages)
- ML/DL model replacement for heuristic logic
- Telecom and banking system integration

---

*Disclaimer: This project is a functional prototype built for the India AI Impact Buildathon. The system demonstrates the feasibility of AI-assisted call fraud detection using heuristic and pattern-based inference.*
