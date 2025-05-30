import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.environ.get("DATA_PATH", os.path.join(PROJECT_ROOT, "data", "data.csv"))
MODEL_PATH = os.environ.get("MODEL_PATH", os.path.join(PROJECT_ROOT, "models", "model.json"))
