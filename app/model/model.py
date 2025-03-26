import pickle
import re
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load the pre-trained model
with open(f"{BASE_DIR}/model-{__version__}.pkl", "rb") as f:
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portuguese",
    "Russian",
    "Spanish",
    "Swedish",
    "Tamil",
    "Turkish",
]


def predict_pipeline(text):
    """
    Preprocess the input text and predict the language.
    """
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])

    return classes[pred[0]]
