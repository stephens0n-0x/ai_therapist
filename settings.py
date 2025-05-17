import os

# -------- window / colours ----------
WIDTH, HEIGHT = 960, 540
FPS = 60
FONT_PATH = None          # use Pygame default font
FONT_SIZE = 18
BG_COLOR   = (30, 30, 40)
TEXT_COLOR = (230, 230, 230)

# -------- Azure Speech (STT & TTS) ---
AZURE_SPEECH_KEY    = os.getenv("AZURE_SPEECH_KEY", "EQPZQXWOFEiKl10nhAtflflhO4Jec23fD5jERsrQJUP8NbxFQ1PKJQQJ99BEAC5RqLJXJ3w3AAAYACOGBN9M")
AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "westeurope")
TTS_VOICE = "en-US-AvaNeural"

AZURE_OPENAI_KEY = "92D3nxKQJoBZhbFpzoJQonR6hHl5k6Swag86fHU4w1iaQ3URfwQ1JQQJ99BEAC5RqLJXJ3w3AAABACOGXqdP"
AZURE_OPENAI_ENDPOINT = "https://ai-therapist-api.openai.azure.com"  
AZURE_OPENAI_DEPLOYMENT = "chat"


# -------- Azure OpenAI ---------------

AZURE_OPENAI_API_VER    = "2024-02-15-preview"

# -------- feature flags --------------
USE_TTS      = True
USE_STT      = True
USE_ENV_PRED = True

LOCAL_ENV_JSON = "StreamingAssets/EnvPredictions/today.env.json"
