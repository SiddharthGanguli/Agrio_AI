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
        mlflow.set_tracking_uri("file:./mlruns")
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
        return {
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(
                y_test, y_pred, average="weighted", zero_division=0
            ),
            "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
            "f1_score": f1_score(
                y_test, y_pred, average="weighted", zero_division=0
            )
        }

    def _log_model_run(self, model_name, model, metrics, X_train, y_pred):
        mlflow.log_param("model_name", model_name)
        mlflow.log_params(model.get_params())
        mlflow.log_metrics(metrics)
        signature = infer_signature(X_train, y_pred)
        mlflow.sklearn.log_model(
            sk_model=model,
            name="model",
            signature=signature,
            input_example=X_train[:5]
        )

    def _train_and_evaluate(self, X_train, y_train, X_test, y_test):
        report = {}
        best_model = None
        best_model_name = None
        best_score = -1

        with mlflow.start_run(run_name="model_training"):
            for model_name, model in self._get_models().items():
                with mlflow.start_run(run_name=model_name, nested=True):
                    logger.info(f"Training {model_name}")
                    model.fit(X_train, y_train)
                    y_pred = model.predict(X_test)
                    metrics = self._evaluate_model(y_test, y_pred)
                    report[model_name] = metrics
                    self._log_model_run(model_name, model, metrics, X_train, y_pred)
                    logger.info(f"{model_name} accuracy: {metrics['accuracy']}")

                    if metrics["accuracy"] > best_score:
                        best_score = metrics["accuracy"]
                        best_model = model
                        best_model_name = model_name

            mlflow.log_param("best_model", best_model_name)
            mlflow.log_metric("best_accuracy", best_score)

        logger.info(f"Best model: {best_model_name}")
        logger.info(f"Best accuracy: {best_score}")
        return best_model, best_model_name, best_score, report

    def _save_model(self, model):
        joblib.dump(model, self.config.model_path)
        logger.info(f"Best model saved at {self.config.model_path}")

    def _save_metrics(self, report):
        with open(self.config.metrics_path, "w") as f:
            json.dump(report, f, indent=4)
        logger.info(f"Metrics saved at {self.config.metrics_path}")
   
    def run(self):
        logger.info("Model training started")
        train_arr, test_arr = self._load_arrays()
        X_train, y_train, X_test, y_test = self._split_input_target(train_arr, test_arr)
        best_model, best_model_name, best_score, report = self._train_and_evaluate(
            X_train, y_train, X_test, y_test
        )
        self._save_model(best_model)
        self._save_metrics(report)
        logger.info("Model training completed")
        return self.config.model_path, best_model_name, best_score
