from app.agents.base import Agent, AgentResult
from app.vision.image_analyzer import ImageAnalyzer

class VisionAgent(Agent):
    name = "vision"
    def __init__(self):
        self.analyzer = ImageAnalyzer()
    def can_handle(self, command: str) -> bool:
        return any(x in command.lower() for x in ("screenshot", "image", "camera", "look at"))
    def run(self, command: str) -> AgentResult:
        return AgentResult(self.name, "success",
            {"status":"vision-input-ready","command":command},
            {"provider_hook":True})
