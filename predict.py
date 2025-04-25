from src_model_io import load_model
from src.predictor import estimate_price_from_input

def main():
    try:
        model = load_model()
        estimate_price_from_input(model)
    except Exception as e:
        print(f"Prediction failed: {e}")

if __name__ = "__main__"):
    main()
