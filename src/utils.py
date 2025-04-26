import math

def normalize(X, mean, std):
    if std == 0:
        raise ValueError("Standard deviation cannot be zero from normalization")
    return (X - mean) / std

def interpret_mse(mse):
    rmse = int(round(math.sqrt(mse)))
    print(f"Root Mean Squared Error (RMSE): {rmse:d}")
    if rmse < 1000:
        print("Excellent ! Very low error.")
    elif rmse < 10000:
        print("Good fit! Acceptable error for this type of problem")
    elif rmse < 100000:
        print("Moderate error. Model could be improved with better features or training")
    else:
        print("High Error ! Model predictions are quite off. Consider using differents parameters on training process")
