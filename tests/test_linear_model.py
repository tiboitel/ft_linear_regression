import sys
import os
import pytest
import numpy as np
from src.linear_model import train_linear_regression, predict_price

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_train_and_predict():
    X = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    model = train_linear_regression(X, y, alpha=0.1, iterations=1000)
    pred = predict_price(6, model)
    assert pred == pytest.approx(12, rel=0.1)
