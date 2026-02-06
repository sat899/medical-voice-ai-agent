from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    environment: str = "local"

    # LiveKit Cloud connection
    livekit_url: str = "wss://localhost:7880"
    livekit_api_key: str = "devkey"
    livekit_api_secret: str = "secret"
    # URL returned to frontend (defaults to livekit_url if unset)
    livekit_public_url: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
