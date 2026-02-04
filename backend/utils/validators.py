def validate_api_key(request, expected_key):
    return request.headers.get("x-api-key") == expected_key


def validate_request_json(data):
    if not data:
        return "Invalid JSON body"

    # Language is now optional - backend will auto-detect it
    required = ["audioFormat", "audioBase64"]
    for field in required:
        if field not in data:
            return f"Missing field: {field}"

    # Strictly accept only MP3 files as requested
    if data["audioFormat"].lower() != "mp3":
        return f"Format {data['audioFormat']} not supported. Only MP3 audio is allowed."

    return None
