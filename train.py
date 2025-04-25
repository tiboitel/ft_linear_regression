import argparse
from src.data_loader import load_data
from src.linear_model import train_linear_regression
from src.model_io import save_model

def main():
    parser = argparse.ArgumentParser(description="Train a linear regression model")
    parser.add_argument('--alpha', type=float, default=0.05, help="Learning Rate (default: 0.05)")
    parser.add_argument('--iterations', type=int, default=1000, help="Number of training iterations (default: 1000)")
    args = parser.parse_args()
    try:
        X, y = load_data()
        model = train_linear_regression(X, y, alpha=args.alpha, iterations=args.iterations)
        save_model(model)
        print("Training complete. Model saved.")
    except Exception as e:
        print(f"Training failed: {e}")

if __name__ == "__main__":
    main()

