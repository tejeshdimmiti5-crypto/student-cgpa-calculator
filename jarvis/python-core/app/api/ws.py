import asyncio
from fastapi import WebSocket, WebSocketDisconnect

async def jarvis_stream(websocket: WebSocket, orchestrator) -> None:
    await websocket.accept()
    await websocket.send_json({"event": "jarvis.connected", "status": "online"})
    try:
        while True:
            message = (await websocket.receive_text()).strip()
            if not message:
                await websocket.send_json({"event": "jarvis.error", "error": "Empty command"})
                continue

            loop = asyncio.get_running_loop()
            event_queue: asyncio.Queue = asyncio.Queue()

            def sink(event):
                payload = {
                    "event": event.topic,
                    "timestamp": event.created_at.isoformat(),
                    **event.payload,
                }
                loop.call_soon_threadsafe(event_queue.put_nowait, payload)

            task = asyncio.create_task(asyncio.to_thread(orchestrator.handle, message, sink))

            while not task.done() or not event_queue.empty():
                try:
                    event = await asyncio.wait_for(event_queue.get(), timeout=0.05)
                    await websocket.send_json(event)
                except asyncio.TimeoutError:
                    continue

            response = await task
            await websocket.send_json({"event": "jarvis.response", "response": response})
    except (WebSocketDisconnect, RuntimeError):
        return
