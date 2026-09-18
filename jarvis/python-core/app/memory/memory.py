class Memory:
    """Temporary working memory. Persistent memory will use PostgreSQL/Redis."""

    def __init__(self) -> None:
        self._store: dict[str, str] = {}

    def remember(self, key: str, value: str) -> None:
        self._store[key] = value

    def recall(self, key: str) -> str | None:
        return self._store.get(key)
