from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from app.config import Settings

@dataclass(frozen=True)
class PersistentMemoryRecord:
    id: int
    key: str
    memory_type: str
    content: Any
    importance: float
    created_at: str

class PostgresMemoryStore:
    """Optional PostgreSQL persistence. Falls back cleanly when DB is unavailable."""

    def __init__(self, database_url: str | None = None) -> None:
        self.database_url = database_url or Settings().database_url
        self._conn = None

    def connect(self):
        if self._conn is None:
            import psycopg
            self._conn = psycopg.connect(self.database_url)
        return self._conn

    def add(self, key: str, value: Any, memory_type: str = "episodic", importance: float = 0.5):
        content = json.dumps(value, ensure_ascii=False, default=str)
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """INSERT INTO jarvis_memory
                       (memory_key, memory_type, content, importance)
                       VALUES (%s, %s, %s, %s)
                       RETURNING id, created_at""",
                    (key, memory_type, content, max(0.0, min(1.0, importance))),
                )
                row = cur.fetchone()
        return row

    def search(self, query: str, limit: int = 5) -> list[PersistentMemoryRecord]:
        pattern = f"%{query}%"
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT id, memory_key, memory_type, content, importance, created_at
                       FROM jarvis_memory
                       WHERE memory_key ILIKE %s OR content ILIKE %s
                       ORDER BY importance DESC, created_at DESC
                       LIMIT %s""",
                    (pattern, pattern, limit),
                )
                rows = cur.fetchall()
        return [
            PersistentMemoryRecord(
                id=row[0], key=row[1], memory_type=row[2],
                content=json.loads(row[3]), importance=row[4],
                created_at=row[5].isoformat(),
            )
            for row in rows
        ]

    def close(self) -> None:
        if self._conn is not None:
            self._conn.close()
            self._conn = None
