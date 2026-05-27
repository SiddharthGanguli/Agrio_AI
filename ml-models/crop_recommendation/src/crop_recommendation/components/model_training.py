import json

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from mlflow.models import infer_signature
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from crop_recommendation.entity.entity import ModelTrainingConfig
from crop_recommendation.logging import get_logger


logger = get_logger("model_training")


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.config.root_dir.mkdir(parents=True, exist_ok=True)

        # MLflow setup
        mlflow.set_tracking_uri("sqlite:///mlflow.db")
        mlflow.set_experiment("Crop Recommendation")

    def _load_arrays(self):
        train_arr = np.load(self.config.train_array_path)
        test_arr = np.load(self.config.test_array_path)

        logger.info("Train and test arrays loaded successfully")

        return train_arr, test_arr

    def _split_input_target(self, train_arr, test_arr):
        X_train = train_arr[:, :-1]
        y_train = train_arr[:, -1].astype(int)

        X_test = test_arr[:, :-1]
        y_test = test_arr[:, -1].astype(int)

        return X_train, y_train, X_test, y_test

    def _get_models(self):
        return {
            "LogisticRegression": LogisticRegression(max_iter=1000),
            "DecisionTree": DecisionTreeClassifier(random_state=42),
            "RandomForest": RandomForestClassifier(random_state=42),
            "KNN": KNeighborsClassifier(),
            "SVC": SVC()
        }

    def _evaluate_model(self, y_test, y_pred):
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

        return metrics

    def _log_model_run(self, model_name, model, metrics):
        mlflow.log_param("model_name", model_name)

        mlflow.log_params(model.get_params())

        mlflow.log_metrics(metrics)

    def _register_best_model(self, best_model, X_train):
        logger.info("Registering best model in MLflow Registry")

        signature = infer_signature(
            X_train,
            best_model.predict(X_train)
        )

        mlflow.sklearn.log_model(
            sk_model=best_model,
            artifact_path="best_model",
            registered_model_name="AGRIO_AI_Crop_Model",
            signature=signature,
            input_example=X_train[:5]
        )

        logger.info("Best model registered successfully")

    def _train_and_evaluate(self, X_train, y_train, X_test, y_test):
        report = {}

        best_model = None
        best_model_name = None
        best_score = -1

        with mlflow.start_run(run_name="model_training"):

            for model_name, model in self._get_models().items():

                with mlflow.start_run(
                    run_name=model_name,
                    nested=True
                ):

                    logger.info(f"Training started for {model_name}")

                    # Train model
                    model.fit(X_train, y_train)

                    # Prediction
                    y_pred = model.predict(X_test)

                    # Metrics
                    metrics = self._evaluate_model(y_test, y_pred)

                    report[model_name] = metrics

                    # MLflow logging
                    self._log_model_run(
                        model_name,
                        model,
                        metrics
                    )

                    logger.info(
                        f"{model_name} accuracy: {metrics['accuracy']}"
                    )

                    # Best model selection
                    if metrics["accuracy"] > best_score:
                        best_score = metrics["accuracy"]
                        best_model = model
                        best_model_name = model_name

            # Log best model info
            mlflow.log_param("best_model", best_model_name)
            mlflow.log_metric("best_accuracy", best_score)

            # Register best model
            self._register_best_model(best_model, X_train)

        logger.info(f"Best model: {best_model_name}")
        logger.info(f"Best accuracy: {best_score}")

        return (
            best_model,
            best_model_name,
            best_score,
            report
        )

    def _save_model(self, model):
        joblib.dump(model, self.config.model_path)

        logger.info(
            f"Best model saved at {self.config.model_path}"
        )

    def _save_metrics(self, report):
        with open(self.config.metrics_path, "w") as f:
            json.dump(report, f, indent=4)

        logger.info(
            f"Metrics saved at {self.config.metrics_path}"
        )

    def _save_best_model_info(
        self,
        best_model_name,
        best_score
    ):
        best_model_info = {
            "best_model": best_model_name,
            "accuracy": best_score
        }

        best_model_info_path = (
            self.config.root_dir / "best_model_info.json"
        )

        with open(best_model_info_path, "w") as f:
            json.dump(best_model_info, f, indent=4)

        logger.info(
            f"Best model info saved at {best_model_info_path}"
        )

    def run(self):
        logger.info("Model training started")

        train_arr, test_arr = self._load_arrays()

        X_train, y_train, X_test, y_test = (
            self._split_input_target(
                train_arr,
                test_arr
            )
        )

        (
            best_model,
            best_model_name,
            best_score,
            report
        ) = self._train_and_evaluate(
            X_train,
            y_train,
            X_test,
            y_test
        )

        self._save_model(best_model)
        
        self._save_metrics(report)

        self._save_best_model_info(
            best_model_name,
            best_score
        )

        logger.info("Model training completed")

        return (
            self.config.model_path,
            best_model_name,
            best_score
        )