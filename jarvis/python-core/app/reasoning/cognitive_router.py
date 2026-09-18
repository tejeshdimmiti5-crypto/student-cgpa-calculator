from app.reasoning.models import CognitiveDecision

class CognitiveRouter:
    """Safety-first intent router for JARVIS agent selection."""
    SENSITIVE = ("delete", "shutdown", "purchase", "send", "remove", "format", "settings")

    def decide(self, command: str, reasoning_steps: list[str]) -> CognitiveDecision:
        text = command.lower().strip()
        if any(x in text for x in self.SENSITIVE):
            return CognitiveDecision("sensitive_action", "computer", None, True, 0.98, "Sensitive intent requires confirmation")
        if any(x in text for x in ("run python", "execute python", "execute code")):
            return CognitiveDecision("code", "code_execution", None, False, 0.94, "Code execution intent")
        if any(x in text for x in ("https://", "http://", "browse", "website", "web page", "visit ")):
            return CognitiveDecision("browser", "browser", None, False, 0.90, "Browser intent")
        if any(x in text for x in ("image", "camera", "screenshot", "look at")):
            return CognitiveDecision("vision", "vision", None, False, 0.84, "Vision intent")
        if any(x in text for x in ("calculate", "system status", "system info", "machine status")):
            return CognitiveDecision("tool", "tool", None, False, 0.92, "Known local tool intent")
        if any(x in text for x in ("research", "search", "find information")):
            return CognitiveDecision("research", "research", None, False, 0.82, "Research intent")
        if any(x in text for x in ("build", "create", "develop", "implement", "code")):
            return CognitiveDecision("coding", "coder", None, False, 0.80, "Coding intent")
        return CognitiveDecision("general", "general", None, False, 0.60, "General intent")
