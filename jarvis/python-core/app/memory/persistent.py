from app.memory.store import MemoryStore
from app.memory.postgres import PostgresMemoryStore

class PersistentMemory:
    """Dual-layer memory: fast local working memory plus durable PostgreSQL history."""

    def __init__(self, database_url: str | None = None) -> None:
        self.local = MemoryStore()
        self.database = PostgresMemoryStore(database_url)

    def add(self, key, value, memory_type="episodic", importance=0.5):
        item = self.local.add(key, value, memory_type, importance)
        try:
            self.database.add(key, value, memory_type, importance)
        except Exception:
            # Local memory remains available if PostgreSQL is temporarily offline.
            pass
        return item

    def search(self, query, limit=5):
        local = self.local.search(query, limit)
        try:
            durable = self.database.search(query, limit)
            return local + durable
        except Exception:
            return local
