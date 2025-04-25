from src.data_loader import load_data
from src.model_io import load_model
from src.plotter import plot_data_and_model

def main():
    try:
        X, y = load_data()
        model = load_model()
        plot_data_and_model(X, y, model)
    except Exception as e:
        print(f"Plotting failed: {e}")

if __name__ == "__main__":
    main()
