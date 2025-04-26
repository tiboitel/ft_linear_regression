import argparse
from src.model_io import load_model
from src.predictor import estimate_price_from_input, evaluate_model_on_data

def main():
    parser = argparse.ArgumentParser(description="Predict car price using trained linear regression model")
    parser.add_argument('--mode', type=str, choices=['interactive', 'batch'],
        default='interactive',
        help="Prediction mode: 'interactive' for single prediction, 'batch' for full dataset evaluation")
    args = parser.parse_args()
    try:
        model = load_model()
        if args.mode == 'interactive':
            estimate_price_from_input(model)
        elif args.mode == 'batch':
            print("Launch of model evaluation out of prediction batch.")
            evaluate_model_on_data(model)
    except Exception as e:
        print(f"Prediction failed: {e}")

if __name__ == "__main__":
    main()
