from src.core.pip.brain.emotions import EmotionsManager
from src.core.pip.eyes import EyeManager
from src.core.scheduler import Scheduler
from src.services.completions.completions_service import CompletionsService
from src.services.homeassistant.homeassistant_service import HomeAssistantService
from src.services.orca.orca_service import OrcaService
from src.services.weather.weather_service import WeatherService


class PipsBrain:
    def __init__(self):
        # Managers
        self.scheduler: Scheduler = Scheduler(self)
        self.eye_manager: EyeManager = EyeManager(self)
        self.emotions_manager: EmotionsManager = EmotionsManager(self)

        # Services
        self.weather_service: WeatherService = WeatherService(self)
        self.homeassistant_service: HomeAssistantService = HomeAssistantService(self)
        self.completions_service: CompletionsService = CompletionsService(self)
        self.tts_service: OrcaService = OrcaService(self)
        self.stt_service = None

        self.scheduler.start()
        self.emotions_manager.set_current_emotion()
