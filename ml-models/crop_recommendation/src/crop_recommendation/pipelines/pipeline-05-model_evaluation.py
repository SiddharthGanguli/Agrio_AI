from pathlib import Path

from crop_recommendation.components.model_evaluation import ModelEvaluation
from crop_recommendation.config.config import ConfigManager
from crop_recommendation.logging import get_logger


logger = get_logger("model_evaluation")

STAGE_NAME = "Model Evaluation"


def main():
    try:
        logger.info(f"{STAGE_NAME} started")

        config_manager = ConfigManager(
            data_path=Path("config/config.yaml")
        )

        model_evaluation_config = (
            config_manager.get_model_evaluation_config()
        )

        model_evaluation = ModelEvaluation(
            config=model_evaluation_config
        )

        metrics = model_evaluation.run()

        logger.info(f"Evaluation Metrics: {metrics}")

        logger.info(
            f"{STAGE_NAME} completed successfully"
        )

    except Exception as e:
        logger.exception(
            f"Error occurred in {STAGE_NAME}: {e}"
        )
        raise e


if __name__ == "__main__":
    main()