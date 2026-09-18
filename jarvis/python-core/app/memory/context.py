from app.memory.store import MemoryStore

class ContextManager:
    """Builds bounded context for reasoning from working and long-term memory."""

    def __init__(self, store: MemoryStore, max_items: int = 8) -> None:
        self.store = store
        self.max_items = max_items

    def build(self, query: str) -> dict:
        memories = self.store.search(query, self.max_items)
        return {
            "query": query,
            "memories": [
                {
                    "key": m.key,
                    "value": m.value,
                    "type": m.memory_type,
                    "importance": m.importance,
                    "created_at": m.created_at,
                }
                for m in memories
            ],
        }
