import base64
import io
from pydub import AudioSegment
import imageio_ffmpeg

AudioSegment.converter = imageio_ffmpeg.get_ffmpeg_exe()

def decode_base64_mp3(base64_audio: str) -> io.BytesIO:
    try:
        audio_bytes = base64.b64decode(base64_audio)
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
        audio = audio.set_channels(1).set_frame_rate(16000)

        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)
        return wav_io
    except Exception as e:
        print(f"DEBUG: Audio decoding error: {e}")
        import traceback
        traceback.print_exc()
        raise ValueError(f"Invalid audio input: {str(e)}")
