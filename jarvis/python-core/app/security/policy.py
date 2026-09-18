from dataclasses import dataclass

@dataclass(frozen=True)
class SecurityDecision:
    allowed: bool
    requires_confirmation: bool
    reason: str

class SecurityPolicy:
    """Default-deny policy for sensitive JARVIS actions."""

    SENSITIVE = {"shutdown", "delete_file", "send_message", "purchase", "system_settings"}

    def evaluate(self, tool_name: str, confirmed: bool = False) -> SecurityDecision:
        if tool_name in self.SENSITIVE and not confirmed:
            return SecurityDecision(False, True, "Explicit user confirmation required.")
        return SecurityDecision(True, False, "Allowed.")
