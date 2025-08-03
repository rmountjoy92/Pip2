from typing import Optional

from fastapi import APIRouter, Query

from src.core.pip import pip

router = APIRouter()


@router.get("/current", summary="get the current weather")
def get_current_weather(
    location: Optional[str] = Query(None, description="optionally provide a location")
):
    return pip.weather_service.get_current_weather(location=location)


# @router.get("/hourly", summary="get today's hourly weather forecast")
# def get_current_weather(
#     location: Optional[str] = Query(None, description="optionally provide a location")
# ):
#     return pip.weather_service.get_hourly_weather(location=location)


@router.get("/forecast", summary="get the weather forcast")
def get_weather_forecast(
    location: Optional[str] = Query(None, description="optionally provide a location")
):
    return pip.weather_service.get_forecast(location=location)
