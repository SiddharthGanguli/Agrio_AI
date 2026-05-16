import pandas as pd
import numpy as np
import joblib

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

from crop_recommendation.entity.entity import DataPreprocessingConfig
from crop_recommendation.logging import get_logger


logger = get_logger("data_preprocessing")


class DataPreprocessing:

    def __init__(self, config: DataPreprocessingConfig):
        self.config = config
        self.pipeline = Pipeline(
            steps=[
                ("imputer", SimpleImputer(strategy="median")),
                ("scaler", MinMaxScaler())
            ]
        )
        self.encoder = LabelEncoder()

    def _load_data(self):
        train_df = pd.read_csv(self.config.train_dir)
        test_df = pd.read_csv(self.config.test_dir)
        logger.info(f"Train shape: {train_df.shape}")
        logger.info(f"Test shape: {test_df.shape}")
        return train_df, test_df

    def _remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_shape = df.shape
        df = df.drop_duplicates()
        removed_rows = initial_shape[0] - df.shape[0]
        logger.info(f"Removed {removed_rows} duplicate rows")
        return df

    def _split_features_target(self, df: pd.DataFrame):
        X = df.drop(columns=["label"])
        y = df["label"]
        return X, y

    def _preprocess_features(self, X_train, X_test):
        X_train = self.pipeline.fit_transform(X_train)
        X_test = self.pipeline.transform(X_test)
        logger.info("Feature preprocessing completed")
        return X_train, X_test

    def _encode_target(self, y_train, y_test):
        y_train = self.encoder.fit_transform(y_train)
        y_test = self.encoder.transform(y_test)
        logger.info("Target encoding completed")
        return y_train, y_test

    def _save_preprocessors(self):
        self.config.root_dir.mkdir(parents=True, exist_ok=True)
        self.config.preprocessed_data_dir.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.pipeline, self.config.preprocessor_path)
        joblib.dump(self.encoder, self.config.label_encoder_path)
        joblib.dump(self.pipeline, self.config.preprocessed_preprocessor_path)
        joblib.dump(self.encoder, self.config.preprocessed_label_encoder_path)
        logger.info("Preprocessors saved successfully")

    def _save_arrays(self, X_train, y_train, X_test, y_test):
        train_arr = np.c_[X_train, y_train]
        test_arr = np.c_[X_test, y_test]

        np.save(self.config.train_array_path, train_arr)
        np.save(self.config.test_array_path, test_arr)
        np.save(self.config.preprocessed_train_array_path, train_arr)
        np.save(self.config.preprocessed_test_array_path, test_arr)
        logger.info("Processed numpy arrays saved successfully")

    def run(self):
        logger.info("Data preprocessing started")

        train_df, test_df = self._load_data()
        train_df = self._remove_duplicates(train_df)
        test_df = self._remove_duplicates(test_df)

        X_train, y_train = self._split_features_target(train_df)
        X_test, y_test = self._split_features_target(test_df)

        X_train, X_test = self._preprocess_features(X_train, X_test)
        y_train, y_test = self._encode_target(y_train, y_test)

        self._save_preprocessors()
        self._save_arrays(X_train, y_train, X_test, y_test)
        logger.info("Data preprocessing completed")

        return self.config.train_array_path, self.config.test_array_path
