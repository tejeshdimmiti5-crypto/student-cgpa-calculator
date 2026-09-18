from fastapi.testclient import TestClient

from app.api.server import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["service"] == "jarvis"


def test_status_endpoint_exposes_runtime():
    response = client.get("/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert data["service"] == "jarvis"
    assert data["agent_count"] >= 12
    assert data["tool_count"] >= 4


def test_command_endpoint_executes_safe_request():
    response = client.post("/v1/command", json={"command": "hello jarvis"})
    assert response.status_code == 200
    body = response.json()
    assert "JARVIS completed" in body["response"]


def test_command_endpoint_blocks_sensitive_request():
    response = client.post("/v1/command", json={"command": "shutdown the computer"})
    assert response.status_code == 200
    assert "Confirmation required" in response.json()["response"]


def test_websocket_command_stream():
    with client.websocket_connect("/v1/ws") as websocket:
        connected = websocket.receive_json()
        assert connected["event"] == "jarvis.connected"

        websocket.send_text("hello jarvis")

        events = []
        while True:
            event = websocket.receive_json()
            events.append(event)
            if event.get("event") == "jarvis.response":
                break

        names = {event.get("event") for event in events}
        assert "jarvis.command.received" in names
        assert "jarvis.plan.created" in names
        assert "jarvis.action.started" in names
        assert "jarvis.action.completed" in names
        assert "jarvis.task.completed" in names
        assert "JARVIS completed" in events[-1]["response"]
