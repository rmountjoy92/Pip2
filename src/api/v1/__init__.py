from fastapi import APIRouter

from . import eyes
from . import homeassistant
from . import weather
from . import timer
from . import completions
from . import radar
from . import stopwatch
from . import notifications

api_router = APIRouter()

api_router.include_router(
    eyes.router, prefix="/eyes", tags=["eyes"], include_in_schema=False
)

api_router.include_router(
    homeassistant.router, prefix="/homeassistant", tags=["homeassistant"]
)
api_router.include_router(weather.router, prefix="/weather", tags=["weather"])
api_router.include_router(timer.router, prefix="/timer", tags=["timer"])
api_router.include_router(
    completions.router,
    prefix="/completions",
    tags=["completions"],
    include_in_schema=False,
)
api_router.include_router(radar.router, prefix="/radar", tags=["radar"])
api_router.include_router(stopwatch.router, prefix="/stopwatch", tags=["stopwatch"])
api_router.include_router(
    notifications.router, prefix="/notifications", tags=["notifications"]
)
