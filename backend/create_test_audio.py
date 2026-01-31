import wave
import struct

sample_rate = 44100
duration = 1  # seconds
n_frames = sample_rate * duration

with wave.open('test_audio.wav', 'w') as obj:
    obj.setnchannels(1)  # mono
    obj.setsampwidth(2)  # 2 bytes per sample
    obj.setframerate(sample_rate)
    
    # Generate silence
    data = struct.pack('<' + ('h'*n_frames), *([0]*n_frames))
    obj.writeframes(data)

print("Created test_audio.wav")
