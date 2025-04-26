import httpx
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


def gerar_resposta(pergunta):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct:free",  
        "messages": [
            {"role": "system", "content": "Você é um assistente amigável e fanático pela FURIA de CS:GO. Responda como um fã."},
            {"role": "user", "content": pergunta}
        ]
    }

    try:
        response = httpx.post(url, headers=headers, json=data, timeout=15)
        response.raise_for_status()
        resposta = response.json()["choices"][0]["message"]["content"]
        return resposta
    except httpx.HTTPStatusError as e:
        print(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
    
    return "Desculpe, não consegui obter uma resposta agora."
