from crop_recommendation.entity.entity import DataIngestionConfig,DataValidationConfig,DataPreprocessingConfig
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
            test_array_path=Path(preprocessing["test_array_path"])
        )
