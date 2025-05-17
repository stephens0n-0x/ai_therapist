import tempfile, pygame, settings, azure.cognitiveservices.speech as speechsdk

_speech_cfg = speechsdk.SpeechConfig(
    subscription=settings.AZURE_SPEECH_KEY,
    region=settings.AZURE_SPEECH_REGION)
_speech_cfg.speech_synthesis_voice_name = settings.TTS_VOICE

def speak(text: str):
    if not settings.USE_TTS:
        return None
    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=_speech_cfg, audio_config=None)
    result = synthesizer.speak_text_async(text).get()
    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("TTS error:", result.reason)
        return None

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(result.audio_data)
        tmp.flush()
        snd = pygame.mixer.Sound(tmp.name)
    snd.play()
    return snd
