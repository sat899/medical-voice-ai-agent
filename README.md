# Medical Voice AI Agent

Real-time voice AI assistant for medical consultations, powered by LiveKit and OpenAI Realtime.

## Run

```bash
docker compose up --build
```

- **Frontend**: http://localhost:3000
- **Health check**: http://localhost:8000/health

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

```
backend/src/
  agent.py            # Voice agent entrypoint – composes tool mixins
  prompts.py          # System prompt / agent persona
  config.py           # Settings from .env
  main.py             # Lightweight FastAPI health check
  tools/
    notes.py          # Tool: save/retrieve clinical notes
    scribe.py         # Tool: transcription & summarisation
    clarifications.py # Tool: clarification questions for clinicians
    actions.py        # Tool: draft letters, order tests, referrals
    appointments.py   # Tool: scheduling & waiting list

frontend/agent-starter-react/  # React frontend (LiveKit agent starter)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the task breakdown per file and how to add new features.
