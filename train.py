from src.data_loader import load_data
from src.linear_model import train_linear_regression
from src.model_io import save_model

def main():
    print("Initialize model training.")
    try:
        X, y = load_data()
        model = train_linear_regression(X, y, 0.5, 1000)
        save_model(model)
        print("Training complete. Model saved.")
    except Exception as e:
        print(f"Training failed: {e}")

if __name__ == "__main__":
    main()

