from fastapi import APIRouter

from src.schemas.timer import TimerResponse, TimerRequest
from src.sockets import socket

router = APIRouter()


@router.post("/set", summary="sets a timer", response_model=TimerResponse)
async def set_timer(req: TimerRequest):
    await socket.manager.emit("timer", {"seconds": req.seconds})
    return TimerResponse(response="Timer open.")
