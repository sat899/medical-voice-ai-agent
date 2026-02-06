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
4. Fill in `frontend/agent-starter-react/.env.local` with the same LiveKit credentials.
5. Run `docker compose up --build`.

## Project structure

| Path | Purpose |
|------|---------|
| `backend/src/agents/voice_agent.py` | Agent entrypoint – composes tool mixins into one agent |
| `backend/src/tools/notes.py` | Tool: save/retrieve clinical notes |
| `backend/src/tools/scribe.py` | Tool: transcription and summarisation |
| `backend/src/tools/clarifications.py` | Tool: clarification questions for clinicians |
| `backend/src/tools/actions.py` | Tool: draft letters, order tests, referrals |
| `backend/src/tools/appointments.py` | Tool: scheduling and waiting list |
| `backend/src/prompts/system.py` | System prompt / agent persona |
| `backend/src/integrations/livekit.py` | LiveKit API client and token generation |
| `backend/src/api/v1/livekit.py` | Token endpoint for frontend to join rooms |
| `backend/src/api/v1/health.py` | Health check endpoint |
| `backend/src/core/config.py` | Settings loaded from `.env` |
| `frontend/agent-starter-react/` | React frontend (LiveKit agent starter) |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the task breakdown per file and how to add new features.
