from app.reasoning.cognitive_router import CognitiveRouter

class CognitiveLoop:
    """Perceive → reason → decide → execute → reflect → remember."""
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.router = CognitiveRouter()

    def run(self, command: str, reasoning):
        decision = self.router.decide(command, reasoning.steps)
        self.orchestrator.events.publish(
            __import__("app.events.bus", fromlist=["Event"]).Event(
                "jarvis.cognitive.decision",
                {"intent":decision.intent,"agent":decision.agent,
                 "confidence":decision.confidence,
                 "requires_confirmation":decision.requires_confirmation}
            )
        )
        return decision
