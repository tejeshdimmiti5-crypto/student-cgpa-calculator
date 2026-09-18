from fastapi import APIRouter
from app.config import Settings

router = APIRouter(prefix="/v1")

settings = Settings()

@router.get("/status")
def status():
    return {
        "service": settings.app_name,
        "environment": settings.environment,
        "llm_provider": settings.llm_provider,
        "model": settings.llm_model,
    }
