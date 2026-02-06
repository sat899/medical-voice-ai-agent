"""
LiveKit integration helpers.

This module centralises how we talk to LiveKit so multiple contributors
can work on agents / services without duplicating connection logic.
"""

from livekit.api import LiveKitAPI, AccessToken
from livekit import rtc

from src.core.config import settings


def get_livekit_api() -> LiveKitAPI:
    """
    Create a LiveKitAPI client bound to the configured server.

    In real usage this will be used for:
    - room management
    - ingress / egress control
    - agent dispatch, etc.
    """
    return LiveKitAPI(
        url=settings.livekit_url,
        api_key=settings.livekit_api_key,
        api_secret=settings.livekit_api_secret,
    )


def create_access_token(identity: str, room: str) -> str:
    """
    Generate an access token for a participant to join a room.

    This is a typical pattern for frontend / client integrations.
    """
    token = AccessToken(
        api_key=settings.livekit_api_key,
        api_secret=settings.livekit_api_secret,
    )
    # NOTE: Adjust grants as needed (publish/subscribe, etc.).
    token.with_identity(identity).with_grants(
        rtc.VideoGrants(room_join=True, room=room)
    )
    return token.to_jwt()

