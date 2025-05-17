import os

# -------- window / colours ----------
WIDTH, HEIGHT = 960, 540
FPS = 60
FONT_PATH = None          # use Pygame default font
FONT_SIZE = 18
BG_COLOR   = (30, 30, 40)
TEXT_COLOR = (230, 230, 230)

# -------- Azure Speech (STT & TTS) ---
AZURE_SPEECH_KEY    = os.getenv("AZURE_SPEECH_KEY", "")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "")
TTS_VOICE = "en-US-AvaNeural"

# -------- Azure OpenAI ---------------
AZURE_OPENAI_KEY        = os.getenv("AZURE_OPENAI_KEY", "")
AZURE_OPENAI_ENDPOINT   = os.getenv("AZURE_OPENAI_ENDPOINT", "")   # e.g. https://your-resource.openai.azure.com
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "") # model deployment name
AZURE_OPENAI_API_VER    = "2024-02-15-preview"

# -------- feature flags --------------
USE_TTS      = True
USE_STT      = True
USE_ENV_PRED = True

LOCAL_ENV_JSON = "StreamingAssets/EnvPredictions/today.env.json"
