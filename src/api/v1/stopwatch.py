from fastapi import APIRouter

from src.schemas import Message
from src.sockets import socket

router = APIRouter()


@router.post("/show", summary="shows the stopwatch on pip", response_model=Message)
async def show_stopwatch():
    await socket.manager.emit("stopwatch")
    return Message(message="Say: Stopwatch opened.")
