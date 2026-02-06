"""
LiveKit Voice Agent – Medical AI Assistant.

Run standalone:
    cd backend
    python -m src.agents.voice_agent dev

It will connect to LiveKit Cloud using the env vars in .env
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
from livekit.agents.llm import function_tool
from livekit.plugins import openai, noise_cancellation

load_dotenv(".env")

# Simple in-memory storage for consultation notes
memory: dict[int, str] = {}


class MedicalVoiceAgent(Agent):
    """Voice-first medical assistant that can remember notes from consultations."""

    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a helpful medical AI assistant communicating via voice. "
                "Keep your responses concise and conversational. "
                "You can remember notes from consultations using the save_note tool. "
                "When asked to recall information, use the get_notes tool. "
                "Do not provide definitive diagnoses – you are a support tool for clinicians."
            ),
        )

    @function_tool
    async def save_note(self, note: str) -> str:
        """Save a clinical note to memory. Use when the user asks you to remember something."""
        note_id = len(memory) + 1
        memory[note_id] = note
        return f"Saved note #{note_id}: {note}"

    @function_tool
    async def get_notes(self) -> str:
        """Retrieve all saved notes. Use when the user asks what you've remembered."""
        if not memory:
            return "No notes saved yet."
        return "\n".join([f"#{nid}: {note}" for nid, note in memory.items()])


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
