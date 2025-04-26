from src.linear_model import predict_price
from src.data_loader import load_data
from src.metrics import compute_mse
from src.utils import interpret_mse

def estimate_price_from_input(model):
    try:
        mileage = float(input("Enter mileage for car: "))
        prediction = predict_price(mileage, model)
        print(f"Estimated price: {round(prediction)}$")
    except ValueError:
        print("Invalid input. Please enter a valid number")

def evaluate_model_on_data(model):
    try:
        X, y_true = load_data()
        y_pred = [predict_price(x, model) for x in X]

        print(f"\n{'Mileage':>10} | {'Actual Price':>13} | {'Predicted Price':>16} | {'Error':>10}")
        print("-" * 60)
        for mileage, actual, predicted in zip(X, y_true, y_pred):
            error = actual - predicted
            print(f"{mileage:10.0f} | {actual:13.2f} | {predicted:16.2f} | {error:10.2f}")

        mse = compute_mse(y_true, y_pred)
        print("\nMean Squared Error (MSE): {:.2f}".format(mse))
        interpret_mse(mse)
    except Exception as e:
        print(f"Evaluation failed: {e}")
