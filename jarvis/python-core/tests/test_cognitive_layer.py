import pytest
from app.reasoning.cognitive_router import CognitiveRouter
from app.memory.semantic import SemanticMemory

def test_router_selects_browser():
    d = CognitiveRouter().decide("open https://example.com", [])
    assert d.agent == "browser"

def test_router_requires_confirmation():
    d = CognitiveRouter().decide("shutdown the computer", [])
    assert d.requires_confirmation is True

def test_semantic_memory_roundtrip():
    memory = SemanticMemory()
    memory.remember("greeting", "hello jarvis")
    results = memory.recall("hello")
    assert results
