WEATHER_CODES = {
    0: "clear",
    1: "mainly_clear",
    2: "partly_cloudy",
    3: "overcast",
    45: "fog",
    48: "freezing_fog",
    51: "light_drizzle",
    53: "moderate_drizzle",
    55: "dense_drizzle",
    56: "freezing_drizzle",
    57: "heavy_freezing_drizzle",
    61: "slight_rain",
    63: "moderate_rain",
    65: "heavy_rain",
    66: "freezing_rain",
    67: "heavy_freezing_rain",
    71: "light_snow",
    73: "moderate_snow",
    75: "heavy_snow",
    77: "flurries",
    80: "light_rain_shower",
    81: "moderate_rain_shower",
    82: "violent_rain_shower",
    85: "light_snow_shower",
    86: "heavy_snow_shower",
    95: "thunderstorm",
    96: "thunderstorm_hail",
    99: "thunderstorm_hail_heavy",
}

WEATHER_DISPLAY_TEXT = {
    "clear": "Clear",
    "mainly_clear": "Mainly Clear",
    "partly_cloudy": "Partly Cloudy",
    "overcast": "Overcast",
    "fog": "Fog",
    "freezing_fog": "Freezing Fog",
    "light_drizzle": "Light Drizzle",
    "moderate_drizzle": "Moderate Drizzle",
    "dense_drizzle": "Dense Drizzle",
    "freezing_drizzle": "Freezing Drizzle",
    "heavy_freezing_drizzle": "Heavy Freezing Drizzle",
    "slight_rain": "Slight Rain",
    "moderate_rain": "Moderate Rain",
    "heavy_rain": "Heavy Rain",
    "freezing_rain": "Freezing Rain",
    "heavy_freezing_rain": "Heavy Freezing Rain",
    "light_snow": "Light Snow",
    "moderate_snow": "Moderate Snow",
    "heavy_snow": "Heavy Snow",
    "flurries": "Flurries",
    "light_rain_shower": "Light Rain Shower",
    "moderate_rain_shower": "Moderate Rain Shower",
    "violent_rain_shower": "Violent Rain Shower",
    "light_snow_shower": "Light Snow Shower",
    "heavy_snow_shower": "Heavy Snow Shower",
    "thunderstorm": "Thunderstorm",
    "thunderstorm_hail": "Thunderstorm with Hail",
    "thunderstorm_hail_heavy": "Heavy Thunderstorm with Hail",
}


def get_weather_code_display_text(weather_code):
    weather_desc = WEATHER_CODES.get(weather_code)
    if not weather_desc:
        return "Unknown Weather"

    return WEATHER_DISPLAY_TEXT.get(weather_desc, "Unknown Weather")
