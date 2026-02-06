from pydantic import BaseModel, Field


class LiveKitTokenRequest(BaseModel):
    """Request body for obtaining a LiveKit access token."""

    room: str = Field(..., description="Room name to join")
    identity: str = Field(..., description="Participant identity (e.g. user id or name)")


class LiveKitTokenResponse(BaseModel):
    """LiveKit URL and JWT for the frontend to connect."""

    url: str = Field(..., description="LiveKit WebSocket URL (wss://...)")
    token: str = Field(..., description="JWT access token for the room")
