import requests
from geopy.geocoders import Nominatim
from typing import Union

from src.core.pip.base_service import PipService
from src.services.weather.weather_code_mapper import WEATHER_CODES


class WeatherService(PipService):
    latitude: str = 35.4307
    longitude: float = -82.5012
    url: str = "https://api.open-meteo.com/v1/forecast"
    geolocator: Nominatim = Nominatim(user_agent="pip")

    def __init__(self, pip):
        super().__init__(pip)
        self.params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/New_York",
        }

    def get_current_weather(self, location: Union[str, None]):
        params = self.params.copy()

        if location is not None:
            l = self.get_location(location)
            params["latitude"] = l.latitude
            params["longitude"] = l.longitude

        params["current"] = [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "wind_gusts_10m",
            "weather_code",
            "precipitation",
            "rain",
            "snowfall",
            "showers",
        ]
        response = self.make_request(params)
        if "weather_code" in response["current"]:
            response["current"]["weather_code"] = WEATHER_CODES.get(
                response["current"]["weather_code"], "unknown"
            )
        return response

    def get_hourly_weather(self, location: Union[str, None]):
        params = self.params.copy()

        if location is not None:
            l = self.get_location(location)
            params["latitude"] = l.latitude
            params["longitude"] = l.longitude

        params["hourly"] = [
            "temperature_2m",
            "relative_humidity_2m",
            "weather_code",
            "precipitation",
        ]
        response = self.make_request(params)
        if "weather_code" in response["hourly"]:
            response["hourly"]["weather_code"] = [
                WEATHER_CODES.get(code, "unknown")
                for code in response["hourly"]["weather_code"]
            ]
        return response

    def get_forecast(self, location: Union[str, None]):
        params = self.params.copy()

        if location is not None:
            l = self.get_location(location)
            params["latitude"] = l.latitude
            params["longitude"] = l.longitude

        params["daily"] = [
            "temperature_2m_max",
            "temperature_2m_min",
            "weather_code",
            "precipitation_probability_max",
            "wind_speed_10m_max",
            "wind_gusts_10m_max",
            "precipitation_sum",
            "rain_sum",
            "snowfall_sum",
            "showers_sum",
            "daylight_duration",
            "sunrise",
            "sunset",
        ]
        response = self.make_request(params)
        if "weather_code" in response["daily"]:
            response["daily"]["weather_code"] = [
                WEATHER_CODES.get(code, "unknown")
                for code in response["daily"]["weather_code"]
            ]

        return response

    def make_request(self, params):
        return requests.get(self.url, params).json()

    def get_location(self, location: str):
        return self.geolocator.geocode(location)
