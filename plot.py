import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/data.csv')
X = data['km'].values.astype(float)
y = data['price'].values.astype(float)

with open('./models/model.json') as f:
    m = json.load(f)
t0, t1 = m['theta0'], m['theta1']
X_mean, X_std = m['X_mean'], m['X_std']

plt.scatter(X, y, label='Data points')

new_X = np.linspace(X.min(), X.max(), 100)
new_X_norm = (new_X - X_mean) / X_std;
preds = t0 + t1 * new_X_norm;
plt.plot(new_X, preds, label='Fitted line')

plt.xlabel('Mileage')
plt.ylabel('Price')
plt.legend()
plt.title('Linear Regression Fit')
plt.show()
