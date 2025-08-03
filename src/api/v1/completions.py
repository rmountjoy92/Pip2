import re
import asyncio
from fastapi import APIRouter

from src.schemas import Message
from src.sockets import socket
from src.core.pip import pip
from src.schemas.completions import CompletionsResponse, CompletionsRequest

router = APIRouter()


def clean_for_orca(text):
    # Step 1: Remove <think> tags and their content
    text = re.sub(r"<think>[\s\S]*?</think>\s*", "", text)

    # Step 2: Remove emojis (common Unicode emoji ranges)
    text = re.sub(
        r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002700-\U000027BF\U00002600-\U000026FF]+",
        "",
        text,
    )

    # Step 3: Keep only alphanumeric characters, spaces, and basic punctuation
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', "", text)

    # Step 4: Clean up extra spaces and normalize
    text = re.sub(r"\s+", " ", text).strip()

    return text


@router.post("/", summary="processes a prompt and makes Pip talk")
async def create_completion(req: CompletionsRequest):
    response = await asyncio.to_thread(
        pip.completions_service.get_completion, prompt=req.prompt
    )
    response = clean_for_orca(response)
    await asyncio.to_thread(pip.tts_service.synthesize_alt, response)
    await socket.manager.emit("new-completion", {"response": response})
    return CompletionsResponse(response=response)


@router.post("/wake", summary="tells Pip's UI to open the voice prompt")
async def wake():
    await socket.manager.emit("wake")
    return Message(message="ok")
