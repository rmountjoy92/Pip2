from fastapi import APIRouter

from src.schemas import Message
from src.sockets import socket

router = APIRouter()


@router.post("/show", summary="shows the radar on pip", response_model=Message)
async def show_radar():
    await socket.manager.emit("radar")
    return Message(message="Radar opened.")
