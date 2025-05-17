import azure.cognitiveservices.speech as speechsdk, settings

def listen() -> str:
    """Record from default mic until pause; return transcript."""
    if not settings.USE_STT:
        return ""
    speech_cfg = speechsdk.SpeechConfig(
        subscription=settings.AZURE_SPEECH_KEY,
        region=settings.AZURE_SPEECH_REGION)
    audio_cfg  = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_cfg, audio_config=audio_cfg)

    print("🎙️  Listening…")
    result = recognizer.recognize_once_async().get()
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    print("STT error:", result.reason)
    return ""
