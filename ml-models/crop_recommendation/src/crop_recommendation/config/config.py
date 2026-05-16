from crop_recommendation.entity.entity import DataIngestionConfig,DataValidationConfig,DataPreprocessingConfig,ModelTrainingConfig,ModelEvaluationConfig
from pathlib import Path   
import yaml
import os 

class ConfigManager :

    def __init__(self,data_path :Path):
        self.config = self._read_yaml(data_path)

    def _read_yaml(self,data_path : Path) -> dict:

        if not data_path.exists():
            raise FileNotFoundError(f"Data path {data_path} does not exist")
        with open(data_path,'r') as yaml_file:
            return yaml.safe_load(yaml_file)
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ingestion = self.config.get("data_ingestion")

        if ingestion is None:
            raise ValueError("Data ingestion config not found in the config file")
        
        root_dir = Path(ingestion.get("root_dir"))
        os.makedirs(root_dir,exist_ok=True)
        
        return DataIngestionConfig(
            root_dir = root_dir,
            source_dir = Path(ingestion.get("source_dir")),
            train_dir = Path(ingestion.get("train_dir")),
            test_dir = Path(ingestion.get("test_dir")),
            test_size = ingestion.get("test_size", 0.2),
            random_state = ingestion.get("random_state", 42)
        )
    
    def get_data_validation_config(self) -> DataValidationConfig:

        validation = self.config.get("data_validation")
        if validation is None:
            raise ValueError("data_validation section missing in config.yaml")

        root_dir = Path(validation["root_dir"])
        os.makedirs(root_dir, exist_ok=True)

        return DataValidationConfig(
            root_dir=root_dir,
            validation_status_file=Path(validation["validation_status_file"]),
            train_dir=Path(validation["train_dir"]),
            schema_file=Path(validation["schema_file"]),
        )
    
    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:

        preprocessing = self.config.get("data_preprocessing")
        if preprocessing is None:
            raise ValueError("data_preprocessing section missing")
        
        root_dir = Path(preprocessing["root_dir"])
        os.makedirs(root_dir,exist_ok=True)

        return DataPreprocessingConfig(
            root_dir=root_dir,
            train_dir=Path(preprocessing["train_dir"]),
            test_dir=Path(preprocessing["test_dir"]),
            preprocessor_path=Path(preprocessing["preprocessor_path"]),
            label_encoder_path=Path(preprocessing["label_encoder_path"]),
            train_array_path=Path(preprocessing["train_array_path"]),
            test_array_path=Path(preprocessing["test_array_path"]),
            preprocessed_data_dir=Path(preprocessing["preprocessed_data_dir"]),
            preprocessed_preprocessor_path=Path(
                preprocessing["preprocessed_preprocessor_path"]
            ),
            preprocessed_label_encoder_path=Path(
                preprocessing["preprocessed_label_encoder_path"]
            ),
            preprocessed_train_array_path=Path(
                preprocessing["preprocessed_train_array_path"]
            ),
            preprocessed_test_array_path=Path(
                preprocessing["preprocessed_test_array_path"]
            )
        )
    def get_model_training_config(self) -> ModelTrainingConfig:
        training = self.config.get("model_training")
        if training is None:
            raise ValueError("model_training section missing")
        root_dir = Path(training["root_dir"])
        os.makedirs(root_dir,exist_ok=True)

        return ModelTrainingConfig(
            root_dir=root_dir,
            train_array_path=Path(training["train_array_path"]),
            test_array_path=Path(training["test_array_path"]),
            model_path=Path(training["model_path"]),
            metrics_path=Path(training["metrics_path"])
        )
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        evaluation = self.config.get("model_evaluation")
        if evaluation is None:raise ValueError("model_evaluation section missing")
        
        root_dir = Path(evaluation["root_dir"])
        os.makedirs(root_dir,exist_ok=True)
        
        return ModelEvaluationConfig(
            root_dir=root_dir,
            model_path=Path(evaluation["model_path"]),
            test_array_path=Path(evaluation["test_array_path"]),
            metrics_file=Path(evaluation["metrics_file"]),
            classification_report_file=Path(evaluation["classification_report_file"]),
            confusion_matrix_file=Path(evaluation["confusion_matrix_file"])
        )