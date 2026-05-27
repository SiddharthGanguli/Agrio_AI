from pathlib import Path
from crop_recommendation.config.config import ConfigManager
from crop_recommendation.components.data_ingestion import DataIngestion
from crop_recommendation.logging import get_logger


STAGE_NAME = "Data Ingestion"
logger = get_logger("data_ingestion")

def main():
    try :
        logger.info(f"{STAGE_NAME} started....")


        config_manager = ConfigManager(data_path=Path("config/config.yaml"))

        data_ingestion_config = config_manager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        train_dir, test_dir = data_ingestion.run()

        logger.info(f"Train data saved at {train_dir} and test data saved at {test_dir}")

        logger.info(f"{STAGE_NAME} completed successfully....")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME} stage: {e}")
        raise e
    
if __name__ == "__main__":
    main()
