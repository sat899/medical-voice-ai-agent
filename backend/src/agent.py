"""
LiveKit Voice Agent – Medical AI Assistant.

Run:
    cd backend
    python -m src.agent dev

Connects to LiveKit Cloud using env vars in .env
(LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET, OPENAI_API_KEY).
"""

from dotenv import load_dotenv

from livekit import agents
from livekit.agents import (
    Agent,
    AgentServer,
    AgentSession,
    JobContext,
    room_io,
)
from livekit.plugins import openai, noise_cancellation

from src.tools.notes import NoteTools
from src.tools.scribe import ScribeTools
from src.tools.clarifications import ClarificationTools
from src.tools.actions import ActionTools
from src.tools.appointments import AppointmentTools
from src.prompts import SYSTEM_INSTRUCTIONS

load_dotenv(".env")


class MedicalVoiceAgent(
    NoteTools,
    ScribeTools,
    ClarificationTools,
    ActionTools,
    AppointmentTools,
    Agent,
):
    """Voice-first medical assistant composed from tool mixins."""

    def __init__(self) -> None:
        super().__init__(instructions=SYSTEM_INSTRUCTIONS)


server = AgentServer()


@server.rtc_session()
async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="alloy",
            model="gpt-4o-realtime-preview",
        ),
    )

    await session.start(
        room=ctx.room,
        agent=MedicalVoiceAgent(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=noise_cancellation.BVC(),
            ),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and let them know you are a medical voice assistant ready to help."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)
