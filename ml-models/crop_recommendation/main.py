from fastapi import FastAPI

from api.middleware import add_cors_middleware, add_logging_middleware
from api.routes.health import router as health_router
from api.routes.model import router as model_router
from api.routes.prediction import router as prediction_router


app = FastAPI(
    title="Crop Recommendation API",
    version="1.0.0",
    description="FastAPI service for crop recommendation model APIs.",
)

add_cors_middleware(app)
add_logging_middleware(app)

app.include_router(health_router)
app.include_router(model_router)
app.include_router(prediction_router)


@app.get("/")
def home():
    return {"service": "crop_recommendation", "message": "API is running"}
