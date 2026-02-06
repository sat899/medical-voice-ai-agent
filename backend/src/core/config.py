from functools import lru_cache
from pydantic import BaseSettings, AnyUrl


class Settings(BaseSettings):
    environment: str = "local"
    database_url: AnyUrl | str

    # LiveKit connection (used by integrations/livekit.py)
    livekit_url: str = "http://livekit:7880"
    livekit_api_key: str = "devkey"
    livekit_api_secret: str = "secret"

    class Config:
        # Use .env.local (committed) for baseline dev config.
        # Developers can override with a private .env if needed.
        env_file = ".env.local"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

