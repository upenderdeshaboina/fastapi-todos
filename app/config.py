from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    # Get the current directory
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/tasks.db"
    API_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Tasks API"

@lru_cache
def get_settings():
    return Settings()