from dataclasses import dataclass

@dataclass
class Reflection:
    success: bool
    confidence: float
    reason: str
    retryable: bool = False

class ReflectionEngine:
    """Evaluates results using explicit success/error/confirmation semantics."""
    def evaluate(self, output: object, expected: str = "") -> Reflection:
        if isinstance(output, dict):
            status = output.get("status")
            if status == "error":
                return Reflection(False, 0.20, str(output.get("error", "tool error")), True)
            if status == "confirmation_required":
                return Reflection(False, 0.10, "Explicit confirmation is required", False)
            if status in {"success", "completed", "ready"}:
                return Reflection(True, 0.90, "Execution completed successfully", False)
        if output is None or str(output).strip() == "":
            return Reflection(False, 0.25, "Empty result", True)
        return Reflection(True, 0.75, "Execution produced a usable result", False)
