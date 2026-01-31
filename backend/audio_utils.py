import os
import tempfile
import base64
import io
from pydub import AudioSegment
import imageio_ffmpeg

AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()

SUPPORTED_FORMATS = [
    "wav", "mp3", "m4a", "ogg", "flac", "webm", "aac"
]

def load_audio_any_format(base64_audio: str, format_hint: str = "mp3") -> str:
    """
    Converts ANY audio format into a standard WAV file path (temp file).
    Adapted to accept Base64 string.
    Returns path to the converted WAV file.
    """
    try:
        audio_bytes = base64.b64decode(base64_audio)
    except Exception:
        raise ValueError("Invalid Base64 audio data")

    suffix = format_hint.lower().replace(".", "")
    if suffix not in SUPPORTED_FORMATS:
        # Try to be lenient, default to mp3 or just let pydub try
        pass 

    # Write input to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as temp_in:
        temp_in.write(audio_bytes)
        temp_in_path = temp_in.name

    try:
        audio = AudioSegment.from_file(temp_in_path)
        audio = audio.set_channels(1).set_frame_rate(16000)

        temp_out = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio.export(temp_out.name, format="wav")
        temp_out_path = temp_out.name
    except Exception as e:
        if os.path.exists(temp_in_path):
            os.remove(temp_in_path)
        raise ValueError(f"Audio conversion failed: {str(e)}")
    
    # Cleanup input temp file
    if os.path.exists(temp_in_path):
        os.remove(temp_in_path)

    return temp_out_path
