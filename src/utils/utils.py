import requests

"""
    Utility functions for interacting with the Ollama API.
"""
def generate_text(model: str, prompt: str) -> str:
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["response"]
