import json
from src.config import MODEL_PATH

def save_model(model: dict):
    try:
        with open(MODEL_PATH, 'w') as f:
            return json.dump(model, f)
    except Exception as e:
        raise IOError(f"Failed to save model: {str(e)}")

def load_model():
    try:
        with open(MODEL_PATH, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    except json.JSONDecodeError:
        raise ValueError("Model file is corrupted or not in JSON format")
