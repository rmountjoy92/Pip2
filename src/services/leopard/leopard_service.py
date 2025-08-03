import os
import pvleopard
from src.config import settings
from src.core.pip.base_service import PipService
from src.paths import static_path


class LeopardService(PipService):
    def __init__(self, pip):
        super().__init__(pip)
        self.orca = pvleopard.create(access_key=settings.PICOVOICE_ACCESS_TOKEN)

    def transcribe(self, audio_file):
        pass
