from fastapi import APIRouter

from src.core.config import settings
from src.integrations.livekit import create_access_token
from src.schemas.livekit import LiveKitTokenRequest, LiveKitTokenResponse

router = APIRouter()


@router.post("/token", response_model=LiveKitTokenResponse)
async def get_livekit_token(payload: LiveKitTokenRequest) -> LiveKitTokenResponse:
    """
    Return the LiveKit WebSocket URL and an access token so a client can join a room.
    Use this from your frontend when connecting to LiveKit Cloud.
    """
    url = settings.livekit_public_url or settings.livekit_url
    token = create_access_token(identity=payload.identity, room=payload.room)
    return LiveKitTokenResponse(url=url, token=token)
