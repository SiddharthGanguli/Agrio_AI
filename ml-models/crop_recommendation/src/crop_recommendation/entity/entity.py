from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir : Path
    source_dir : Path
    train_dir : Path
    test_dir : Path
    test_size : float
    random_state : int

@dataclass
class DataValidationConfig:
    root_dir: Path
    validation_status_file: Path
    train_dir: Path
    schema_file: Path

@dataclass
class DataPreprocessingConfig:
    root_dir: Path
    train_dir: Path
    test_dir: Path
    preprocessor_path: Path
    label_encoder_path: Path
    train_array_path: Path
    test_array_path: Path
    preprocessed_data_dir: Path
    preprocessed_preprocessor_path: Path
    preprocessed_label_encoder_path: Path
    preprocessed_train_array_path: Path
    preprocessed_test_array_path: Path

@dataclass
class ModelTrainingConfig:
    root_dir: Path
    train_array_path: Path
    test_array_path: Path
    model_path: Path
    metrics_path: Path