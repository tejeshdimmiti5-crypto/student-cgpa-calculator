from fastapi import WebSocket

async def jarvis_stream(websocket: WebSocket, orchestrator) -> None:
    await websocket.accept()
    await websocket.send_json({"event": "jarvis.connected"})
    try:
        while True:
            message = await websocket.receive_text()
            response = orchestrator.handle(message)
            await websocket.send_json({
                "event": "jarvis.response",
                "response": response,
            })
    except Exception:
        await websocket.close()
