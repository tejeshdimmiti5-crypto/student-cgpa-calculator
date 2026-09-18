from fastapi import FastAPI, WebSocket
from pydantic import BaseModel, Field

from app.core.orchestrator import JarvisOrchestrator
from app.api.routes import router as status_router
from app.api.ws import jarvis_stream

app = FastAPI(title="JARVIS Cognitive Gateway", version="1.0.0")
jarvis = JarvisOrchestrator()
app.include_router(status_router)

class CommandRequest(BaseModel):
    command: str = Field(min_length=1, max_length=10000)

class CommandResponse(BaseModel):
    response: str

@app.get("/health")
def health():
    return {"status": "online", "service": "jarvis", "version": "1.0.0"}

@app.post("/v1/command", response_model=CommandResponse)
def command(request: CommandRequest):
    return CommandResponse(response=jarvis.handle(request.command))

@app.websocket("/v1/ws")
async def websocket(websocket: WebSocket):
    await jarvis_stream(websocket, jarvis)
