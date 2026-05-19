import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib
from fastapi import APIRouter, HTTPException, status

from api.schemas.model_schema import (
    ArtifactStatus,
    ModelInfoResponse,
    ModelMetrics,
    ModelVersionResponse,
)


router = APIRouter(prefix="/model", tags=["Model"])

PROJECT_ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = PROJECT_ROOT / "artifacts/model_training/model.pkl"
METRICS_PATH = PROJECT_ROOT / "artifacts/model_training/metrics.json"
PREPROCESSOR_PATH = PROJECT_ROOT / "artifacts/data_preprocessing/preprocessor.pkl"
LABEL_ENCODER_PATH = PROJECT_ROOT / "artifacts/data_preprocessing/label_encoder.pkl"
FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
SERVICE_NAME = "crop_recommendation"
API_VERSION = "1.0.0"
MODEL_VERSION = "1.0.0"


@router.get("/info", response_model=ModelInfoResponse)
def get_model_info() -> ModelInfoResponse:
    metrics_report = _load_metrics()
    best_model_name, best_metrics = _get_best_model(metrics_report)
    model = _load_model()

    return ModelInfoResponse(
        service=SERVICE_NAME,
        model_name=model.__class__.__name__,
        best_model_name=best_model_name,
        metrics=ModelMetrics(**best_metrics),
        features=FEATURES,
        artifacts=_get_artifact_status(),
    )


@router.get("/version", response_model=ModelVersionResponse)
def get_model_version() -> ModelVersionResponse:
    return ModelVersionResponse(
        service=SERVICE_NAME,
        api_version=API_VERSION,
        model_version=MODEL_VERSION,
        model_updated_at=_get_file_updated_at(MODEL_PATH),
    )


def _load_model() -> Any:
    if not MODEL_PATH.exists():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Model artifact not found at {MODEL_PATH}",
        )
    return joblib.load(MODEL_PATH)


def _load_metrics() -> dict[str, dict[str, float]]:
    if not METRICS_PATH.exists():
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Metrics file not found at {METRICS_PATH}",
        )

    with METRICS_PATH.open("r", encoding="utf-8") as metrics_file:
        return json.load(metrics_file)


def _get_best_model(metrics_report: dict[str, dict[str, float]]) -> tuple[str, dict[str, float]]:
    if not metrics_report:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Metrics file is empty",
        )

    return max(
        metrics_report.items(),
        key=lambda item: item[1].get("accuracy", 0.0),
    )


def _get_artifact_status() -> ArtifactStatus:
    return ArtifactStatus(
        model_available=MODEL_PATH.exists(),
        preprocessor_available=PREPROCESSOR_PATH.exists(),
        label_encoder_available=LABEL_ENCODER_PATH.exists(),
    )


def _get_file_updated_at(path: Path) -> datetime | None:
    if not path.exists():
        return None
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
