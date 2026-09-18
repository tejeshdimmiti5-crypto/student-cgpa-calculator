import pytest

from app.core.orchestrator import JarvisOrchestrator
from app.runtime.runtime import AgentRuntime
from app.runtime.executor import ActionExecutor
from app.reasoning.actions import Action

def test_runtime_has_core_agents_and_tools():
    runtime = AgentRuntime()
    names = {x["name"] for x in runtime.agent_status()}
    assert {"planner", "research", "coder", "tester", "validator", "browser", "vision", "computer", "code", "tools", "general", "orchestrator"} <= names
    assert runtime.tool_status()

def test_sensitive_action_requires_confirmation():
    runtime = AgentRuntime()
    executor = ActionExecutor(runtime)
    result = executor.execute(Action("x", "tool", "shutdown", {"command": "shutdown"} , requires_confirmation=True))
    assert result["status"] == "confirmation_required"

def test_orchestrator_builds_safe_plan():
    jarvis = JarvisOrchestrator()
    response = jarvis.handle("hello jarvis")
    assert "JARVIS plan completed" in response

def test_orchestrator_blocks_sensitive_request():
    jarvis = JarvisOrchestrator()
    response = jarvis.handle("shutdown the computer")
    assert "Confirmation required" in response
