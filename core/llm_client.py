import openai, settings, functools

openai.api_type       = "azure"
openai.api_key        = settings.AZURE_OPENAI_KEY
openai.api_base       = settings.AZURE_OPENAI_ENDPOINT
openai.api_version    = settings.AZURE_OPENAI_API_VER

_chat = functools.partial(
    openai.chat.completions.create,
    engine=settings.AZURE_OPENAI_DEPLOYMENT,
    temperature=0.7)

def chat(messages):
    """messages = [{'role':'system','content':'…'}, …]"""
    resp = _chat(messages=messages)
    return resp.choices[0].message.content
