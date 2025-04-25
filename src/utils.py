def normalize(X, mean, std):
    if std == 0:
        raise ValueError("Standard deviation cannot be zero from normalization")
    return (X - mean) / std
