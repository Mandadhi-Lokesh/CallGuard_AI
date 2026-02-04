import base64
import re

def decode_base64_audio(b64_string):
    b64_string = re.sub(r"^data:audio/.+;base64,", "", b64_string)
    b64_string = b64_string.replace("\n", "").replace(" ", "")

    missing_padding = len(b64_string) % 4
    if missing_padding:
        b64_string += "=" * (4 - missing_padding)

    return base64.b64decode(b64_string)
