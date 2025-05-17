import openai, settings, functools

# 👇 Add this block before calling OpenAI
openai.api_type = "azure"
openai.api_key = settings.AZURE_OPENAI_KEY
openai.api_base = settings.AZURE_OPENAI_ENDPOINT  # <--- this line is required
openai.api_version = settings.AZURE_OPENAI_API_VER

_chat = functools.partial(
    openai.chat.completions.create,
    engine=settings.AZURE_OPENAI_DEPLOYMENT,
    temperature=0.7,
)
