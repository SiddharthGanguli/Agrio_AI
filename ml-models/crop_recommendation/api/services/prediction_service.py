from functools import lru_cache

from api.schemas.prediction_schema import CropPredictionRequest, CropPredictionResponse
from prediction.prediction import CustomData, PredictPipeline


@lru_cache(maxsize=1)
def get_prediction_pipeline() -> PredictPipeline:
    return PredictPipeline()


def predict_crop(input_data: CropPredictionRequest) -> CropPredictionResponse:
    custom_data = CustomData(
        N=input_data.N,
        P=input_data.P,
        K=input_data.K,
        temperature=input_data.temperature,
        humidity=input_data.humidity,
        ph=input_data.ph,
        rainfall=input_data.rainfall,
    )

    prediction = get_prediction_pipeline().predict_with_confidence(custom_data)[0]
    return CropPredictionResponse(**prediction)
