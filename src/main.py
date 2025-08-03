import asyncio
import signal
import sys

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger

from src.api.v1 import api_router
from src.config import settings
from src.core.pip import pip
from src.sockets import socket

app = FastAPI(title=settings.PROJECT_NAME, version=f"v-{settings.APP_VERSION}")


@app.get("/", include_in_schema=False)
async def index() -> RedirectResponse:
    """
    Pip eyes home page redirect
    """
    return RedirectResponse(f"{settings.API_V1_STR}/eyes/page")


app.include_router(api_router, prefix=settings.API_V1_STR)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

socket.init_manager(app)

app.mount("/static/audio", StaticFiles(directory="src/static/audio"), name="audio")

pip.scheduler.init_app(app)

signal.signal(signal.SIGINT, pip.scheduler.signal_handler)
signal.signal(signal.SIGTERM, pip.scheduler.signal_handler)

# Loguru
logger.remove()
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add(
    "data/app.log", rotation="10 MB", retention="10 days", level="INFO", enqueue=True
)


@app.on_event("startup")
def startup_event():
    asyncio.create_task(pip.eye_manager.process_idle())


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True if settings.ENV == "local" else False,
    )
