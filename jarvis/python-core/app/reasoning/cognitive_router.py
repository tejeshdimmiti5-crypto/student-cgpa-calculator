from app.reasoning.models import CognitiveDecision

class CognitiveRouter:
    """Deterministic safety-first router used after LLM reasoning."""
    SENSITIVE = ("delete", "shutdown", "purchase", "send", "remove", "format", "settings")
    def decide(self, command: str, reasoning_steps: list[str]) -> CognitiveDecision:
        text = command.lower()
        if any(x in text for x in self.SENSITIVE):
            return CognitiveDecision("sensitive_action", "computer", None, True, 0.95, "Sensitive intent requires confirmation")
        if any(x in text for x in ("calculate", "system status", "system info", "machine status")):
            return CognitiveDecision("tool", "tool", "auto", False, 0.90, "Known local tool intent")
        if any(x in text for x in ("https://", "http://", "browse", "website", "web page", "visit ")):
            return CognitiveDecision("browser", "browser", None, False, 0.88, "Browser intent detected")
        if any(x in text for x in ("run python", "execute python", "execute code")):
            return CognitiveDecision("code", "code_execution", None, False, 0.92, "Code execution intent detected")
        if any(x in text for x in ("image", "camera", "screenshot", "look at")):
            return CognitiveDecision("vision", "vision", None, False, 0.82, "Vision intent detected")
        if any(x in text for x in ("research", "search", "find information")):
            return CognitiveDecision("research", "research", None, False, 0.80, "Research intent detected")
        return CognitiveDecision("general", "general", None, False, 0.60, "General conversational intent")
