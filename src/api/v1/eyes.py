from fastapi import APIRouter, Request, Security
from fastapi.responses import StreamingResponse, HTMLResponse, JSONResponse

from src import schemas
from src.api.deps import verify_api_key
from src.core import templates, pip
from src.enums import ExpressionTypes, AnimationTypes

router = APIRouter()


@router.get("/page")
async def page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "eyes_feed.html", {"request": request}, status_code=200
    )


@router.get("/stream")
async def stream() -> StreamingResponse:
    """
    Stream pip's eyes as an image
    """
    return StreamingResponse(
        pip.eye_manager.generate_eye_steam(),
        status_code=200,
        media_type="multipart/x-mixed-replace; boundary=frame",
    )


@router.post("/expression/set", response_model=schemas.Message)
async def set_expression(expression_name: ExpressionTypes = "Neutral") -> JSONResponse:
    """
    Set Pip's expression directly
    """
    pip.eye_manager.set_next_expression(expression_name)
    return JSONResponse({"message": "ok"}, 200)


@router.post("/animation/play", response_model=schemas.Message)
async def play_animation(
    animation_name: AnimationTypes,
) -> JSONResponse:
    """
    Play an eye animation
    """
    await pip.eye_manager.animate(animation_name)
    return JSONResponse({"message": "ok"}, 200)
