import logging
import os
import time
from logging.handlers import RotatingFileHandler

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

LOG_DIR = "logs"
LOG_FORMAT = (
    "%(asctime)s | "
    "%(name)s | "
    "%(levelname)s | "
    "%(filename)s:%(lineno)d | "
    "%(message)s"
)


def get_api_logger() -> logging.Logger:
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("crop_recommendation.api")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = RotatingFileHandler(
        os.path.join(LOG_DIR, "api.log"),
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


logger = get_api_logger()


def add_cors_middleware(app: FastAPI) -> None:
    allowed_origins = _get_allowed_origins()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def add_logging_middleware(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_requests(request: Request, call_next):
        start_time = time.perf_counter()

        try:
            response = await call_next(request)
        except Exception:
            process_time = time.perf_counter() - start_time
            logger.exception(
                "Request failed | method=%s path=%s client=%s duration=%.4fs",
                request.method,
                request.url.path,
                request.client.host if request.client else None,
                process_time,
            )
            raise

        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.4f}"

        log_level = _get_log_level(response.status_code)
        logger.log(
            log_level,
            "Request completed | method=%s path=%s status_code=%s client=%s duration=%.4fs",
            request.method,
            request.url.path,
            response.status_code,
            request.client.host if request.client else None,
            process_time,
        )

        return response


def _get_allowed_origins() -> list[str]:
    origins = os.getenv("CORS_ALLOWED_ORIGINS")
    if origins:
        return [origin.strip() for origin in origins.split(",") if origin.strip()]

    return [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


def _get_log_level(status_code: int) -> int:
    if status_code >= 500:
        return 40
    if status_code >= 400:
        return 30
    return 20
