from datetime import datetime

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str = Field(..., description="Shows whether the API is running")
    service: str = Field(..., description="Name of this API service")
    version: str = Field(..., description="Current API version")
    timestamp: datetime = Field(..., description="Current server time in UTC")
