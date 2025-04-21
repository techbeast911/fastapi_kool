from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional, List, Dict, Any


class Settings(BaseSettings):
    DATABASE_URL: str 
    JWT_SECRET_KEY : str
    JWT_ALGORITHM: str
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


Config= Settings()