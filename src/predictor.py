from src.linear_model import predict_price
from src.metrics import compute_mse

def estimate_price_from_input(model):
    try:
        mileage = float(input("Enter mileage for car: "))
        prediction = predict_price(mileage, model)
        print(f"Estimated price: {round(prediction)}$")
    except ValueError:
        print("Invalid input. Please enter a valid number")

