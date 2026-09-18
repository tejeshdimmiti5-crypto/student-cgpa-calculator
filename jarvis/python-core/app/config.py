import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
    app_name: str = "JARVIS"
    environment: str = os.getenv("JARVIS_ENV","development")
    llm_provider: str = os.getenv("JARVIS_LLM_PROVIDER","mock")
    llm_model: str = os.getenv("JARVIS_LLM_MODEL","gemini-3.8-flash")
    database_url: str = os.getenv("DATABASE_URL","postgresql://jarvis:jarvis@localhost:5432/jarvis")
    redis_url: str = os.getenv("REDIS_URL","redis://localhost:6379/0")
