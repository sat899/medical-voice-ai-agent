"""
Lightweight FastAPI app – health check only.

The real work happens in agent.py (the LiveKit voice agent).
This exists so docker compose can expose a health endpoint for monitoring.
"""

from fastapi import FastAPI

app = FastAPI(title="Medical Voice AI Agent", version="0.1.0")


@app.get("/health")
async def health():
    return {"status": "ok"}
