from fastapi import APIRouter
import os

router = APIRouter()

@router.get("/v1/status")
def status():
    runtime = None
    try:
        from app.api.server import jarvis
        runtime = jarvis.runtime
        agents = runtime.agent_status()
    except Exception:
        agents = []
    return {
        "service": "jarvis",
        "environment": os.getenv("JARVIS_ENV", "development"),
        "provider": os.getenv("JARVIS_LLM_PROVIDER", "mock"),
        "model": os.getenv("JARVIS_LLM_MODEL", "gemini-2.0-flash"),
        "agents": agents,
        "agent_count": len(agents),
    }
