from datetime import datetime, timezone

from fastapi import APIRouter

from api.schemas.health_schema import HealthResponse


router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="crop_recommendation",
        version="1.0.0",
        timestamp=datetime.now(timezone.utc),
    )
