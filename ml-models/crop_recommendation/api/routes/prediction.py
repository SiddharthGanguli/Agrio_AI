from fastapi import APIRouter, HTTPException, status

from api.schemas.prediction_schema import (
    CropPredictionRequest,
    CropPredictionResponse,
)
from api.services.prediction_service import predict_crop


router = APIRouter(prefix="/prediction", tags=["Prediction"])


@router.post("", response_model=CropPredictionResponse)
def create_prediction(input_data: CropPredictionRequest) -> CropPredictionResponse:
    try:
        prediction = predict_crop(input_data)
    except FileNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(error),
        ) from error
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        ) from error

    return prediction
