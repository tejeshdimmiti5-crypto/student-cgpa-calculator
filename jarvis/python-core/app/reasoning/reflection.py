from dataclasses import dataclass

@dataclass
class Reflection:
    success: bool
    confidence: float
    reason: str
    retryable: bool = False

class ReflectionEngine:
    """Evaluates execution results and decides whether JARVIS should retry or recover."""

    def evaluate(self, output: object, expected: str = "") -> Reflection:
        if isinstance(output, dict) and output.get("status") == "error":
            return Reflection(False, 0.2, str(output.get("error", "tool error")), True)
        if isinstance(output, dict) and output.get("status") == "confirmation_required":
            return Reflection(False, 0.1, "Explicit confirmation is required", False)
        if output is None or str(output).strip() == "":
            return Reflection(False, 0.25, "Empty result", True)
        return Reflection(True, 0.85, "Execution produced a usable result", False)
