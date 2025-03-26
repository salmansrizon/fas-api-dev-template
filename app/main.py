from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version

# Initiate FastAPI app
app = FastAPI()

# Mount static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates
templates = Jinja2Templates(directory="templates")

# Define Pydantic models for input/output
class TextIn(BaseModel):
    text: str  # Input text


class PredictionOut(BaseModel):
    language: str  # Predicted language


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the Gradio-like UI for the homepage.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn):
    """
    Endpoint to predict the language of the input text.
    """
    language = predict_pipeline(payload.text)
    return {"language": language}