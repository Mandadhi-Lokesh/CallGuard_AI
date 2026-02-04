import asyncio
import edge_tts
import os
import random

OUTPUT_DIR = "training/data/ai"
TARGET_COUNT = 500

# Base sentences for generation
SENTENCES = {
    "en": [
        "The quick brown fox jumps over the lazy dog.",
        "Your authentication code is 4829.",
        "Please confirm your identity by pressing one.",
        "We have detected suspicious activity on your account.",
        "This is a call from your bank regarding a recent transaction.",
        "Congratulations, you have won a special prize.",
        "Hello, this is technical support calling about your computer.",
        "Artificial intelligence is transforming the way we live.",
        "The weather today is sunny with a chance of rain.",
        "To speak with a representative, please stay on the line.",
        "Your package has been delivered to your front door.",
        "Verify your email address to complete the registration.",
        "This call may be recorded for quality assurance purposes.",
        "Payment received, thank you for your business.",
        "Please update your password immediately.",
        "An OTP has been sent to your registered mobile number.",
        "Do not share this code with anyone, including bank officials.",
        "Your account will be suspended if you do not act now.",
        "We are calling to verify a recent purchase of five hundred dollars.",
        "Press star to repeat this message."
    ],
    "hi": [
        "नमस्ते, मैं बैंक से बोल रहा हूँ, क्या मैं आपसे बात कर सकता हूँ?",
        "आपका ओटीपी 5643 है, इसे किसी के साथ साझा न करें।",
        "आपके खाते में संदिग्ध गतिविधि देखी गई है।",
        "कृपया अपनी पहचान की पुष्टि करने के लिए एक दबाएं।",
        "बधाई हो, आपने एक लॉटरी जीती है।",
        "यह कॉल गुणवत्ता आश्वासन के लिए रिकॉर्ड की जा सकती है।",
        "अपने आधार कार्ड को लिंक करने के लिए यहाँ क्लिक करें।",
        "क्या आप क्रेडिट कार्ड बनवाना चाहते हैं?",
        "टेक्निकल सपोर्ट टीम से बात करने के लिए होल्ड करें।",
        "आपका पार्सल आज डिलीवर कर दिया जाएगा।"
    ],
    "ta": [
        "வணக்கம், உங்கள் வங்கிக் கணக்கில் சிக்கல் உள்ளது.",
        "உங்கள் ஓடிபி எண் 1234, இதை யாருடனும் பகிர வேண்டாம்.",
        "கடன் அட்டை பெற விருப்பமா?",
        "தயவுசெய்து உங்கள் அடையாளத்தை சரிபார்க்கவும்.",
        "இது ஒரு முக்கியமான அறிவிப்பு.",
        "உங்கள் பரிசுப் பொருளைப் பெற கீழே உள்ள எண்ணை அழைக்கவும்.",
        "உங்கள் கணக்கு முடக்கப்பட்டுள்ளது.",
        "மேலும் விவரங்களுக்கு எங்களை தொடர்பு கொள்ளவும்.",
        "இணைய பாதுகாப்பு மிகவும் முக்கியமானது.",
        "நீங்கள் வென்றுள்ளீர்கள், வாழ்த்துக்கள்."
    ],
    "te": [
        "నమస్కారం, మీ బ్యాంక్ ఖాతా వివరాలను సరిచూసుకోండి.",
        "మీకు ఒక ముఖ్యమైన సందేశం ఉంది.",
        "దయచేసి మీ ఓటీపీ ఎవరికీ చెప్పకండి.",
        "మీ లోన్ అప్లికేషన్ ఆమోదించబడింది.",
        "ఆన్‌లైన్ మోసాల పట్ల జాగ్రత్తగా ఉండండి.",
        "కస్టమర్ కేర్ ప్రతినిధితో మాట్లాడటానికి వేచి ఉండండి.",
        "ఈ కాల్ రికార్డ్ చేయబడుతోంది.",
        "మీ క్రెడిట్ కార్డ్ పరిమితి పెంచబడింది.",
        "బహుమతి గెలుచుకోవడానికి ఇప్పుడు కాల్ చేయండి.",
        "మీ ఇంటర్నెట్ సేవ రేపు నిలిపివేయబడుతుంది."
    ],
    "ml": [
        "നമസ്കാരം, ഇത് ബാങ്കിൽ നിന്നുള്ള വിളിയാണ്.",
        "നിങ്ങളുടെ ഒടിപി നമ്പർ ആരുമായും പങ്കിടരുത്.",
        "നിങ്ങളുടെ അക്കൗണ്ട് മരവിപ്പിച്ചിരിക്കുന്നു.",
        "കൂടുതൽ വിവരങ്ങൾക്ക് ഒന്ന് അമർത്തുക.",
        "നിങ്ങൾക്ക് ലോട്ടറി അടിച്ചിരിക്കുന്നു.",
        "ദയവായി നിങ്ങളുടെ വിവരങ്ങൾ പുതുക്കുക.",
        "ഓൺലൈൻ തട്ടിപ്പുകൾക്കെതിരെ ജാഗ്രത പാലിക്കുക.",
        "നിങ്ങളുടെ പാഴ്സൽ എത്തിയിട്ടുണ്ട്.",
        "ഇതൊരു ഓട്ടോമേറ്റഡ് സന്ദേശമാണ്.",
        "അടിയന്തിരമായി കസ്റ്റമർ കെയറുമായി ബന്ധപ്പെടുക."
    ]
}

# Extensive list of neural voices
VOICES = [
    # English
    "en-US-AriaNeural", "en-US-GuyNeural", "en-US-JennyNeural", "en-US-EricNeural", 
    "en-US-ChristopherNeural", "en-GB-SoniaNeural", "en-GB-RyanNeural", 
    "en-AU-NatashaNeural", "en-AU-WilliamNeural", "en-IN-NeerjaNeural", "en-IN-PrabhatNeural",
    # Hindi
    "hi-IN-SwaraNeural", "hi-IN-MadhurNeural",
    # Tamil
    "ta-IN-PallaviNeural", "ta-IN-ValluvarNeural",
    # Telugu
    "te-IN-ShrutiNeural", "te-IN-MohanNeural",
    # Malayalam
    "ml-IN-SobhanaNeural", "ml-IN-MidhunNeural"
]

async def generate_dataset():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Determine start index based on existing files
    existing_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith("ai_") and f.endswith(".mp3")]
    start_index = len(existing_files)
    
    if start_index >= TARGET_COUNT:
        print(f"Target of {TARGET_COUNT} files already reached. No new files generated.")
        return

    print(f"Resuming generation from index {start_index} to {TARGET_COUNT} in {OUTPUT_DIR}...")
    
    tasks = []
    
    for i in range(start_index, TARGET_COUNT):
        filename = f"ai_{i:04d}.mp3"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        # Random selection
        voice = random.choice(VOICES)
        
        # Determine language from voice code for better text matching
        lang_code = voice.split("-")[0]
        if lang_code == "hide": lang_code = "hi" # edge case if needed
        
        # Simple fallback matching
        if "en-" in voice: text_pool = SENTENCES["en"]
        elif "hi-" in voice: text_pool = SENTENCES["hi"]
        elif "ta-" in voice: text_pool = SENTENCES["ta"]
        elif "te-" in voice: text_pool = SENTENCES["te"]
        elif "ml-" in voice: text_pool = SENTENCES["ml"]
        else: text_pool = SENTENCES["en"]
            
        text = random.choice(text_pool)
        
        # Apply random rate and pitch adjustments for "different fonts" / variety
        rate_adj = random.randint(-10, 10)
        pitch_adj = random.randint(-5, 5)
        rate_str = f"{rate_adj:+d}%"
        pitch_str = f"{pitch_adj:+d}Hz"
        
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate_str, pitch=pitch_str)
            tasks.append(communicate.save(filepath))
        except Exception as e:
             print(f"Error preparing task for {filename}: {e}")
        
        # Batch processing to avoid overwhelming
        if len(tasks) >= 10:
            try:
                await asyncio.gather(*tasks)
                print(f"Generated up to {filename}")
            except Exception as e:
                print(f"Batch generation failed: {e}")
                # Wait a bit before retrying or continuing to avoid rate limits/locks
                await asyncio.sleep(2)
            finally:
                tasks = []

    if tasks:
        await asyncio.gather(*tasks)
        
    print(f"Completed! Total files in folder: {len(os.listdir(OUTPUT_DIR))}")

if __name__ == "__main__":
    asyncio.run(generate_dataset())