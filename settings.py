import os

# -------- window / colours ----------
WIDTH, HEIGHT = 960, 540
FPS = 60
FONT_PATH = None          # use Pygame default font
FONT_SIZE = 18
BG_COLOR   = (30, 30, 40)
TEXT_COLOR = (230, 230, 230)

# -------- Azure Speech (STT & TTS) ---
AZURE_SPEECH_KEY    = os.getenv("AZURE_SPEECH_KEY", "ENTER-YOUR-SPEECH-KEY")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "ENTER-YOUR-SPEECH-KEY-REGION")
TTS_VOICE = "ENTER-VOICE"

AZURE_OPENAI_KEY = "ENTER-YOUR-API"
AZURE_OPENAI_ENDPOINT = "ENTER-YOUR-API-ENDPOINT"  
AZURE_OPENAI_DEPLOYMENT = "chat"


# -------- Azure OpenAI ---------------

AZURE_OPENAI_API_VER    = "2024-02-15-preview"

# -------- feature flags --------------
USE_TTS      = True
USE_STT      = True
USE_ENV_PRED = True

LOCAL_ENV_JSON = "StreamingAssets/EnvPredictions/today.env.json"
