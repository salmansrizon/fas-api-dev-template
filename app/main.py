# importing libs
from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version

# initiate fast API
app = FastAPI()


# Declaring Model input class
class TextIn(BaseModel):
    text: str  # only taking string input for the model


# Declaring Model Output class
class PredictionOut(BaseModel):
    language: str  # Model's prediction output


@app.get("/")
def home():
    return {"health Check": "ok", "Model version": model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"langage": language}
