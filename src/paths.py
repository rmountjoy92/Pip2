import os
from pathlib import Path


src_path = Path(__file__).parent
static_path = os.path.join(src_path, "static")
static_audio_path = os.path.join(static_path, "audio")
