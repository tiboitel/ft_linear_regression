import pandas as pd
from src.config import DATA_PATH

def load_data():
    try:
        df = pd.read_csv(DATA_PATH)
        X = df['km'].astype(float).values
        y = df['price'].astype(float).values
        return X, y
    except FileNotFoundError:
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")
    except Exception as e:
        raise RuntimeError(f"Failed to load data: {str(e)}")
