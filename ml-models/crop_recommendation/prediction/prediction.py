from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

import joblib
import pandas as pd


FEATURE_COLUMNS = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass
class CustomData:
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

    def get_data_as_dataframe(self) -> pd.DataFrame:
        data = {
            "N": [self.N],
            "P": [self.P],
            "K": [self.K],
            "temperature": [self.temperature],
            "humidity": [self.humidity],
            "ph": [self.ph],
            "rainfall": [self.rainfall],
        }
        return pd.DataFrame(data, columns=FEATURE_COLUMNS)


class PredictPipeline:
    def __init__(
        self,
        model_path: str | Path | None = None,
        preprocessor_path: str | Path | None = None,
        label_encoder_path: str | Path | None = None,
    ) -> None:
        self.model_path = Path(model_path or PROJECT_ROOT / "artifacts/model_training/model.pkl")
        self.preprocessor_path = Path(
            preprocessor_path or PROJECT_ROOT / "artifacts/data_preprocessing/preprocessor.pkl"
        )
        self.label_encoder_path = Path(
            label_encoder_path or PROJECT_ROOT / "artifacts/data_preprocessing/label_encoder.pkl"
        )
        self._model = None
        self._preprocessor = None
        self._label_encoder = None

    def predict(
        self,
        input_data: CustomData | pd.DataFrame | Mapping[str, float] | Iterable[Mapping[str, float]],
    ) -> list[str]:
        dataframe = self._to_dataframe(input_data)
        transformed_data = self.preprocessor.transform(dataframe)
        encoded_predictions = self.model.predict(transformed_data)
        predictions = self.label_encoder.inverse_transform(encoded_predictions.astype(int))
        return predictions.tolist()

    def predict_with_confidence(
        self,
        input_data: CustomData | pd.DataFrame | Mapping[str, float] | Iterable[Mapping[str, float]],
    ) -> list[dict[str, float | str | None]]:
        dataframe = self._to_dataframe(input_data)
        transformed_data = self.preprocessor.transform(dataframe)
        encoded_predictions = self.model.predict(transformed_data)
        predictions = self.label_encoder.inverse_transform(encoded_predictions.astype(int))

        confidences = [None] * len(predictions)
        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba(transformed_data)
            confidences = probabilities.max(axis=1).round(2).tolist()

        return [
            {"crop": crop, "confidence": confidence}
            for crop, confidence in zip(predictions.tolist(), confidences)
        ]

    @property
    def model(self):
        if self._model is None:
            self._model = self._load_artifact(self.model_path, "model")
        return self._model

    @property
    def preprocessor(self):
        if self._preprocessor is None:
            self._preprocessor = self._load_artifact(self.preprocessor_path, "preprocessor")
        return self._preprocessor

    @property
    def label_encoder(self):
        if self._label_encoder is None:
            self._label_encoder = self._load_artifact(self.label_encoder_path, "label encoder")
        return self._label_encoder

    def _to_dataframe(
        self,
        input_data: CustomData | pd.DataFrame | Mapping[str, float] | Iterable[Mapping[str, float]],
    ) -> pd.DataFrame:
        if isinstance(input_data, CustomData):
            dataframe = input_data.get_data_as_dataframe()
        elif isinstance(input_data, pd.DataFrame):
            dataframe = input_data.copy()
        elif isinstance(input_data, Mapping):
            dataframe = pd.DataFrame([input_data])
        else:
            dataframe = pd.DataFrame(input_data)

        missing_columns = [column for column in FEATURE_COLUMNS if column not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Missing required input columns: {missing_columns}")

        dataframe = dataframe[FEATURE_COLUMNS].copy()
        for column in FEATURE_COLUMNS:
            dataframe[column] = pd.to_numeric(dataframe[column], errors="raise")

        return dataframe

    @staticmethod
    def _load_artifact(path: Path, artifact_name: str):
        if not path.exists():
            raise FileNotFoundError(f"Could not find {artifact_name} artifact at: {path}")
        return joblib.load(path)


if __name__ == "__main__":
    sample_input = CustomData(
        N=37,
        P=78,
        K=79,
        temperature=19.95264829,
        humidity=14.82633099,
        ph=7.786366322,
        rainfall=88.6810311,
    )
    print(PredictPipeline().predict(sample_input))
