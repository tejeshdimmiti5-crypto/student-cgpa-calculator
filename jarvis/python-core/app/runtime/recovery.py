from dataclasses import dataclass

@dataclass
class RecoveryDecision:
    retry: bool
    attempt: int
    reason: str

class RecoveryManager:
    def decide(self, attempt: int, max_attempts: int, retryable: bool) -> RecoveryDecision:
        if retryable and attempt < max_attempts:
            return RecoveryDecision(True, attempt + 1, "Retryable failure; re-executing within attempt budget")
        return RecoveryDecision(False, attempt, "Retry budget exhausted or failure is non-retryable")
