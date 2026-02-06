"""
Tool: Clinical Notes
Owner: [assign a team member]

Provides tools for saving and retrieving clinical notes during a consultation.
"""

from livekit.agents.llm import function_tool

# Simple in-memory store – replace with a database when ready.
memory: dict[int, str] = {}


class NoteTools:
    """Mixin that gives the agent the ability to remember consultation notes."""

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
