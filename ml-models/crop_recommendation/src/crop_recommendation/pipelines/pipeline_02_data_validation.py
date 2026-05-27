from pathlib import Path

from crop_recommendation.components.data_validation import DataValidation
from crop_recommendation.config.config import ConfigManager
from crop_recommendation.logging import get_logger

logger = get_logger("data_validation")

STAGE_NAME = "Data Validation Stage"


def main():
    try:
        logger.info(f"{STAGE_NAME} started...")

        config_manager = ConfigManager(
            data_path=Path("config/config.yaml")
        )

        data_validation_config = config_manager.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)

        status = data_validation.run()

        if not status:
            raise Exception("Data validation failed")

        logger.info(f"{STAGE_NAME} completed successfully.")

    except Exception as e:
        logger.exception(f"Error in {STAGE_NAME}")
        raise e


if __name__ == "__main__":
    main()
