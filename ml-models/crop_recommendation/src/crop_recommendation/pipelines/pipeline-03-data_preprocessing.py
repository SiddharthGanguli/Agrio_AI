from pathlib import Path

from crop_recommendation.components.data_preprocessing import DataPreprocessing
from crop_recommendation.config.config import ConfigManager
from crop_recommendation.logging import get_logger


logger = get_logger("data_preprocessing")
STAGE_NAME = "Data Preprocessing"


def main():
    try:
        logger.info(f"{STAGE_NAME} started")

        config_manager = ConfigManager(
            data_path=Path("config/config.yaml")
        )
        data_preprocessing_config = (
            config_manager.get_data_preprocessing_config()
        )
        data_preprocessing = DataPreprocessing(
            config=data_preprocessing_config
        )

        train_arr_path, test_arr_path = data_preprocessing.run()

        logger.info(f"Train array saved at: {train_arr_path}")
        logger.info(f"Test array saved at: {test_arr_path}")
        logger.info(f"{STAGE_NAME} completed successfully")

    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e


if __name__ == "__main__":
    main()
