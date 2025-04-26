def compute_mse(y_true, y_pred):
    if len(y_true) != len(y_pred):
        raise ValueError("Input vectors must have the same length.")
    error = [(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)]
    mse = sum(error) / len(error)
    return mse
