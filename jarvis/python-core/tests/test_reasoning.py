from app.reasoning.engine import ReasoningEngine
from app.reasoning.models import ReasoningRequest

def test_reasoning_plan():
    plan = ReasoningEngine().create_plan(ReasoningRequest("analyze project"))
    assert plan.goal == "analyze project"
    assert plan.steps == ["analyze project"]
    assert 0.0 <= plan.confidence <= 1.0
