from datetime import datetime

from pydantic import BaseModel, Field


class ModelMetrics(BaseModel):
    accuracy: float = Field(..., description="Model accuracy score")
    precision: float = Field(..., description="Weighted precision score")
    recall: float = Field(..., description="Weighted recall score")
    f1_score: float = Field(..., description="Weighted F1 score")


class ArtifactStatus(BaseModel):
    model_available: bool = Field(..., description="Whether model.pkl exists")
    preprocessor_available: bool = Field(..., description="Whether preprocessor.pkl exists")
    label_encoder_available: bool = Field(..., description="Whether label_encoder.pkl exists")


class ModelInfoResponse(BaseModel):
    service: str = Field(..., description="Name of this API service")
    model_name: str = Field(..., description="Saved model class name")
    best_model_name: str = Field(..., description="Best model name based on metrics")
    metrics: ModelMetrics = Field(..., description="Metrics for the best model")
    features: list[str] = Field(..., description="Input features expected by the model")
    artifacts: ArtifactStatus = Field(..., description="Availability of required artifacts")


class ModelVersionResponse(BaseModel):
    service: str = Field(..., description="Name of this API service")
    api_version: str = Field(..., description="Current API version")
    model_version: str = Field(..., description="Current model version")
    model_updated_at: datetime | None = Field(
        default=None,
        description="Last modified time of model.pkl in UTC",
    )
