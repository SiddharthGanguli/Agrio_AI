from pydantic import BaseModel, Field


class CropPredictionRequest(BaseModel):
    N: float = Field(..., ge=0, description="Nitrogen value in the soil")
    P: float = Field(..., ge=0, description="Phosphorus value in the soil")
    K: float = Field(..., ge=0, description="Potassium value in the soil")
    temperature: float = Field(..., description="Temperature in Celsius")
    humidity: float = Field(..., ge=0, le=100, description="Humidity percentage")
    ph: float = Field(..., ge=0, le=14, description="Soil pH value")
    rainfall: float = Field(..., ge=0, description="Rainfall value in mm")


class CropPredictionResponse(BaseModel):
    crop: str = Field(..., description="Recommended crop name")
    confidence: float | None = Field(
        default=None,
        ge=0,
        le=1,
        description="Prediction confidence score between 0 and 1",
    )
