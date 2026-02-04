import librosa
import io
import soundfile as sf
import numpy as np

def decode_mp3(audio_bytes):
    """
    Decodes audio bytes into waveform and sample rate.
    Supports MP3, WAV, and other formats handled by librosa/soundfile.
    """
    audio_stream = io.BytesIO(audio_bytes)
    
    try:
        # Try loading with soundfile first (faster for WAV/RAW)
        waveform, sr = sf.read(audio_stream)
        # Convert to mono if stereo
        if len(waveform.shape) > 1:
            waveform = np.mean(waveform, axis=1)
        return waveform, sr
    except Exception as e:
        print(f"Soundfile failed, falling back to librosa: {e}")
        # Fallback to librosa which uses multiple backends
        audio_stream.seek(0)
        waveform, sr = librosa.load(audio_stream, sr=None, mono=True)
        return waveform, sr
