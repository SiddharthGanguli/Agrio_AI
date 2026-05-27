import json
import joblib
import numpy as np
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay
)

from crop_recommendation.entity.entity import ModelEvaluationConfig
from crop_recommendation.logging import get_logger


logger = get_logger("model_evaluation")


class ModelEvaluation:

    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        self.config.root_dir.mkdir(parents=True, exist_ok=True)

    def _load_model(self):
        model = joblib.load(self.config.model_path)
        logger.info("Model loaded successfully")
        return model

    def _load_test_array(self):
        test_arr = np.load(self.config.test_array_path)

        X_test = test_arr[:, :-1]
        y_test = test_arr[:, -1].astype(int)

        logger.info("Test array loaded successfully")
        return X_test, y_test

    def _evaluate_model(self, model, X_test, y_test):
        y_pred = model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            ),
            "recall": recall_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            ),
            "f1_score": f1_score(
                y_test,
                y_pred,
                average="weighted",
                zero_division=0
            )
        }

        report = classification_report(
            y_test,
            y_pred,
            zero_division=0
        )

        logger.info("Model evaluation completed")

        return metrics, report

    def _save_metrics(self, metrics):
        with open(self.config.metrics_file, "w") as file:
            json.dump(metrics, file, indent=4)

        logger.info("Metrics saved successfully")

    def _save_classification_report(self, report):
        with open(self.config.classification_report_file, "w") as file:
            file.write(report)

        logger.info("Classification report saved successfully")

    def _save_confusion_matrix(self, model, X_test, y_test):
        disp = ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)

        disp.figure_.savefig(self.config.confusion_matrix_file)

        plt.close()

        logger.info("Confusion matrix saved successfully")

    def run(self):

        logger.info("Model evaluation started")

        model = self._load_model()

        X_test, y_test = self._load_test_array()

        metrics, report = self._evaluate_model(
            model,
            X_test,
            y_test
        )

        self._save_metrics(metrics)

        self._save_classification_report(report)

        self._save_confusion_matrix(
            model,
            X_test,
            y_test
        )

        with mlflow.start_run():

            mlflow.log_metrics(metrics)

            mlflow.log_artifact(
                self.config.metrics_file
            )

            mlflow.log_artifact(
                self.config.classification_report_file
            )

            mlflow.log_artifact(
                self.config.confusion_matrix_file
            )

            mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model"
            )

            logger.info(
                "Artifacts and metrics logged to MLflow"
            )

        logger.info(
            "Model evaluation completed"
        )

        return metrics