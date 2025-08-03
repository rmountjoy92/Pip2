import secrets

from pydantic.v1 import BaseSettings


# these can be overwritten in .env
class Settings(BaseSettings):
    APP_VERSION: str = "local-dev"
    BASE_URL: str = "http://localhost:8000"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Pip Server"
    ENV: str = "prod"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///data/pip.db"
    MASTER_KEY: str = secrets.token_urlsafe(32)

    # Completions
    COMPLETIONS_SERVICE_URL: str = "http://localhost:3000"
    COMPLETIONS_API_TOKEN: str = ""
    COMPLETIONS_MODEL: str = "qwen3:14b"

    # Home Assistant
    HOME_ASSISTANT_API_KEY: str = ""
    HOME_ASSISTANT_URL: str = "http://homeassistant.local:8123"

    # Picovoice
    PICOVOICE_ACCESS_TOKEN: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
