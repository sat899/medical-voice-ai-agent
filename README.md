# Medical Voice AI Agent

Real-time voice AI assistant for medical consultations, powered by LiveKit and OpenAI Realtime.

## Run

```bash
docker compose up --build
```

- **API**: http://localhost:8000
- **Docs**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

## Setup

1. Create a project at [LiveKit Cloud](https://cloud.livekit.io).
2. Copy the **URL**, **API Key**, and **API Secret** from Project Settings.
3. Fill in `backend/.env`:
   ```
   LIVEKIT_URL=wss://your-project.livekit.cloud
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   OPENAI_API_KEY=your_openai_key
   ```
4. Run `docker compose up --build`.

## Project structure

| Path | Purpose |
|------|---------|
| `backend/src/agents/voice_agent.py` | LiveKit voice agent (OpenAI Realtime + noise cancellation) |
| `backend/src/integrations/livekit.py` | LiveKit API client and token generation |
| `backend/src/api/v1/health.py` | Health check endpoint |
| `backend/src/api/v1/livekit.py` | Token endpoint for frontend to join rooms |
| `backend/src/core/config.py` | Settings loaded from `.env` |
| `backend/src/main.py` | FastAPI app entry |
| `frontend/` | Frontend UI |
