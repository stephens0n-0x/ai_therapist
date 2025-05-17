import requests, tempfile, pygame, settings, os
from pydub import AudioSegment

TTS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{settings.VOICE_ID}"

HEAD = {
    "xi-api-key": settings.ELEVEN_KEY,
    "Content-Type": "application/json"
}

def speak(text):
    if not settings.USE_TTS:
        return
    payload = {"text": text, "model_id": "eleven_multilingual_v2"}
    r = requests.post(TTS_URL, headers=HEAD, json=payload, timeout=30)
    r.raise_for_status()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(r.content)
        tmp.flush()
        sound = pygame.mixer.Sound(tmp.name)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.wait(50)
        os.unlink(tmp.name)
