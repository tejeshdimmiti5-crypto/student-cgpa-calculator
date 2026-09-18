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
        tools = runtime.tool_status()
    except Exception:
        agents = []
        tools = []

    return {
        "service": "jarvis",
        "status": "online",
        "environment": os.getenv("JARVIS_ENV", "development"),
        "provider": os.getenv("JARVIS_LLM_PROVIDER", "mock"),
        "model": os.getenv("JARVIS_LLM_MODEL", "configured"),
        "agents": agents,
        "agent_count": len(agents),
        "tools": tools,
        "tool_count": len(tools),
        "capabilities": [
            "perception", "reasoning", "memory", "rag", "dag-planning",
            "multi-agent-runtime", "secure-tools", "reflection-recovery",
            "browser-boundary", "vision-boundary", "voice-boundary",
        ],
    }
