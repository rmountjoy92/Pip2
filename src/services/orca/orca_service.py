import os
import subprocess
import pvorca
from src.config import settings
from src.core.pip.base_service import PipService
from src.paths import static_audio_path, src_path


class OrcaService(PipService):
    orca_path = os.path.join(src_path, "services", "orca")

    def __init__(self, pip):
        super().__init__(pip)
        self.orca = pvorca.create(
            access_key=settings.PICOVOICE_ACCESS_TOKEN,
            model_path=os.path.join(self.orca_path, "orca_params_en_male.pv"),
        )

    def synthesize(self, text: str):
        self.orca.synthesize_to_file(
            text=text,
            output_path=os.path.join(static_audio_path, "response.wav"),
            speech_rate=0.9,
        )

    def synthesize_alt(self, text: str):
        command = (
            f'echo "{text.replace('"', '\\"')}" | piper-tts --model /usr/share/piper-voices/en/en_US/danny/low/en_US-danny-low.onnx '
            f'--output_file "{os.path.join(static_audio_path, "response.wav")}"'
        )
        subprocess.run(command, shell=True, check=True)
