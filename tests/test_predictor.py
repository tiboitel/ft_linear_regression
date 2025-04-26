import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.predictor import predict_price

def test_predict_price_normalized():
    model = {"theta0": 2.0, "theta1": 3.0, "X_mean": 5.0, "X_std": 2.0}
    prediction = predict_price(7, model)
    expected = 2 + 3 * ((7 - 5) / 2)
    assert abs(prediction - expected) < 1e-6

def test_predict_price_invalid_model():
    with pytest.raises(KeyError):
        predict_price(10, {})
