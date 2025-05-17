import os
WIDTH, HEIGHT = 960, 540
FPS = 60
FONT_PATH = "assets/font/PressStart2P.ttf"
FONT_SIZE = 18
BG_COLOR = (30, 30, 40)
TEXT_COLOR = (230, 230, 230)

OPENAI_KEY     = os.getenv("OPENAI_KEY",     "")   # or groq
ELEVEN_KEY     = os.getenv("ELEVEN_KEY",     "")
VOICE_ID       = "Matilda"

# toggle features for fast iteration
USE_TTS        = True
USE_ENV_PRED   = False     # flip to True when env_predict.py is ready
