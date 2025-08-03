import requests

from src.config import settings
from src.core.pip.base_service import PipService
from src.schemas.homeassistant import CommandResponse


class HomeAssistantService(PipService):
    url: str = settings.HOME_ASSISTANT_URL
    api_token: str = settings.HOME_ASSISTANT_API_KEY

    def __init__(self, pip):
        super().__init__(pip)

    def run_command(self, command: str) -> CommandResponse:
        response = requests.post(
            f"{self.url}/api/conversation/process",
            headers={
                "Authorization": f"Bearer {self.api_token}",
                "Content-Type": "application/json",
            },
            json={"text": command, "language": "en"},
        )
        response_data = response.json()
        return CommandResponse(
            response=response_data.get("response", {})
            .get("speech", {})
            .get("plain", {})
            .get("speech", "No response message")
        )
