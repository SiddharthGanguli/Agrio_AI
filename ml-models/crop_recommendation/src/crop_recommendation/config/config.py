from crop_recommendation.entity.entity import DataIngestionConfig
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
