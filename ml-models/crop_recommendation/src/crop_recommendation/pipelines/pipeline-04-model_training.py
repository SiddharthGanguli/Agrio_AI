from pathlib import Path

from crop_recommendation.components.model_training import ModelTraining
from crop_recommendation.config.config import ConfigManager
from crop_recommendation.logging import get_logger


logger = get_logger("model_training")
STAGE_NAME = "Model Training"


def main():
    try:
        logger.info(f"{STAGE_NAME} started")
        config_manager = ConfigManager(data_path=Path("config/config.yaml"))
        model_training_config = config_manager.get_model_training_config()
        model_training = ModelTraining(config=model_training_config)
        model_path, best_model_name, best_score = model_training.run()
        logger.info(f"Best model: {best_model_name}")
        logger.info(f"Best accuracy: {best_score}")
        logger.info(f"Model saved at: {model_path}")
        logger.info(f"{STAGE_NAME} completed successfully")
    except Exception as e:
        logger.exception(f"Error occurred in {STAGE_NAME}: {e}")
        raise e


if __name__ == "__main__":
    main()
