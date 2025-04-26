import numpy as np
from src.utils import normalize
from src.metrics import compute_mse

def train_linear_regression(X, y, alpha=0.05, iterations=1000):
    m = len(y)
    theta0, theta1 = 0.0, 0.0
    X_mean, X_std = X.mean(), X.std()
    X_norm = normalize(X, X_mean, X_std)
    y_pred = 0.0

    for i in range(iterations):
        y_pred = theta0 + theta1 * X_norm;
        errors = y_pred - y;
        grad0 = (1/m) * np.sum(errors);
        grad1 = (1/m) * np.sum(errors * X_norm);

        theta0 -= alpha * grad0;
        theta1 -= alpha * grad1;

        if i % 100 == 0:
            cost = (1/(2*m)) * np.sum(errors**2)
            print(f"Iter {i:4d}: cost={cost:.4f}, theta0={theta0:.4f}, theta1={theta1:.4f}")

    y_pred = [theta0 + theta1 * ((xi - X_mean) / X_std) for xi in X]
    training_mse = compute_mse(y, y_pred)
    print(f"Mean Squared Error on training set: {training_mse:.4f}")
    return {
        'theta0': theta0,
        'theta1': theta1,
        'X_mean': X_mean,
        'X_std': X_std
    }

def predict_price(x, model):
    x_norm = normalize(x, model['X_mean'], model['X_std'])
    return model['theta0'] + model['theta1'] * x_norm
