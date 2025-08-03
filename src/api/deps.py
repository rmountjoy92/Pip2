from typing import Generator

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from src.config import settings
from src.database.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def verify_api_key(api_key: str = Security(APIKeyHeader(name="X-API-Key"))):
    if api_key != settings.MASTER_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")
