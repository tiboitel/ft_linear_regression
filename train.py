import json
import numpy as np
import pandas as pd

data = pd.read_csv('data/data.csv');
X = data['km'].values.astype(float)
y = data['price'].values.astype(float)
m = len(y)

X_mean, X_std = X.mean(), X.std()
X_norm = (X - X_mean) / X_std;

theta0, theta1 = 0.0, 0.0
alpha = 0.01 # learning rate
num_iters = 1000

def predict(x0, x1):
    return x0 + x1 * x;

for i in range(num_iters):
    y_pred = theta0 + theta1 * X_norm;
    errors = y_pred - y;
    grad0 = (1/m) * np.sum(errors);
    grad1 = (1/m) * np.sum(errors * X_norm);

    theta0 -= alpha * grad0;
    theta1 -= alpha * grad1;

    if i % 100 == 0:
        cost = (1/(2*m)) * np.sum(errors**2)
        print(f"Iter {i:4d}: cost={cost:.4f}, theta0={theta0:.4f}, theta1={theta1:.4f}")

model = {
    'theta0': theta0,
    'theta1': theta1,
    'X_mean': X_mean,
    'X_std': X_std
}

with open('./models/model.json', 'w') as f:
    json.dump(model, f)

print("Training complete. Model saved to models/model.json")
