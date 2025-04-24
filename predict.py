import json

with open('models/model.json') as f:
    model = json.load(f)
theta0 = model['theta0']
theta1 = model['theta1']
X_mean = model['X_mean']
X_std = model['X_std']

mileage = float(input("Enter mileage of the car: "))
x_norm = (mileage - X_mean) / X_std
y_pred = theta0 + theta1 * x_norm
print(f"Estimated price: ${y_pred:.2f}")
