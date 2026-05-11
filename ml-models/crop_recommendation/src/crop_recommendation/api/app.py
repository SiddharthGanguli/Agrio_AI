from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "project": "crop_recommendation"
    }