import requests, json, settings

CHAT_ENDPOINT = "https://api.openai.com/v1/chat/completions"

HEAD = {
    "Authorization": f"Bearer {settings.OPENAI_KEY}",
    "Content-Type": "application/json"
}

def chat(messages, model="gpt-3.5-turbo"):
    body = {
        "model": model,
        "temperature": 0.7,
        "messages": messages
    }
    r = requests.post(CHAT_ENDPOINT, headers=HEAD, json=body, timeout=30)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
