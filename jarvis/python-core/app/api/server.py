from fastapi import FastAPI
from pydantic import BaseModel

from app.core.orchestrator import JarvisOrchestrator

app = FastAPI(title="JARVIS Cognitive Gateway", version="0.1.0")
jarvis = JarvisOrchestrator()

class CommandRequest(BaseModel):
    command: str

class CommandResponse(BaseModel):
    response: str

@app.get("/health")
def health():
    return {"status": "online", "service": "jarvis"}

@app.post("/v1/command", response_model=CommandResponse)
def command(request: CommandRequest):
    return CommandResponse(response=jarvis.handle(request.command))
