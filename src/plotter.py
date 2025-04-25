import numpy as np
import matplotlib.pyplot as plt


def plot_data_and_model(X, y, model):
    plt.scatter(X, y, label='Data points')

    new_X = np.linspace(X.min(), X.max(), 100)
    new_X_norm = (new_X - model['X_mean']) / model['X_std']
    preds = model['theta0'] + model['theta1'] * new_X_norm;
    plt.plot(new_X, preds, label='Fitted line', color='red')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    plt.title('Linear Regression Fit')
    plt.legend()
    plit.grid(True)
    plt.tight_layout()
    plt.show()
