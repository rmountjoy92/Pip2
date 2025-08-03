from fastapi import APIRouter

from src.core.pip import pip
from src.schemas.homeassistant import CommandResponse, CommandRequest


router = APIRouter()


@router.post(
    "/command",
    summary="Forwards smart home prompts to Home Assistant. Handles all smart home commands. Also handles questions about the state of devices in the user's smart home.",
    response_model=CommandResponse,
)
def run_command(req: CommandRequest):
    return pip.homeassistant_service.run_command(req.prompt)
