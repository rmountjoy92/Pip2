import requests

from typing import List
from src.config import settings

from src.core.pip.base_service import PipService


class CompletionsService(PipService):
    url: str = settings.COMPLETIONS_SERVICE_URL
    api_token: str = settings.COMPLETIONS_API_TOKEN
    model: str = settings.COMPLETIONS_MODEL

    messages: List = [
        {
            "role": "system",
            "content": "Your response will be synthesized into audio. Always use speakable words. For numbers it's mandatory to use words for the numbers and 'point' for a decimal, example never say 75.25 always say 'seventy five point two five'.",
        },
    ]

    def __init__(self, pip):
        super().__init__(pip)

    def get_completion(self, prompt: str) -> str:
        self.messages.append({"role": "user", "content": prompt})

        url = f"{self.url}/api/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }
        data = {
            "stream": False,
            "model": self.model,
            "messages": self.messages,
            "tool_ids": ["server:0"],
        }

        response = requests.post(url, headers=headers, json=data).json()
        print(response)

        content = response["choices"][0]["message"]["content"]

        self.messages.append({"role": "assistant", "content": content})

        return content
