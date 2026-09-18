from enum import Enum

class RuntimeState(str, Enum):
    IDLE="idle"
    PLANNING="planning"
    EXECUTING="executing"
    OBSERVING="observing"
    REFLECTING="reflecting"
    RECOVERING="recovering"
    COMPLETED="completed"
    BLOCKED="blocked"
    FAILED="failed"

class RuntimeStateMachine:
    def __init__(self):
        self.state = RuntimeState.IDLE

    def transition(self, state: RuntimeState):
        self.state = state
        return self.state
