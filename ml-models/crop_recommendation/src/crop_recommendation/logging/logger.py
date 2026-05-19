import os
import logging
from logging.handlers import RotatingFileHandler


LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


LOG_FORMAT = (
    "%(asctime)s | "
    "%(name)s | "
    "%(levelname)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)

def get_logger(stage_name: str) -> logging.Logger:
    logger_name = f"crop_recommendation.{stage_name}"
    stage_logger = logging.getLogger(logger_name)
    stage_logger.setLevel(logging.INFO)
    stage_logger.propagate = False

    if stage_logger.handlers:
        return stage_logger

    formatter = logging.Formatter(LOG_FORMAT)
    log_file = os.path.join(LOG_DIR, f"{stage_name}.log")

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    stage_logger.addHandler(file_handler)
    stage_logger.addHandler(console_handler)
    return stage_logger


logger = get_logger("data_ingestion")
