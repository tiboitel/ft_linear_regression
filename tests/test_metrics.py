import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.metrics import compute_mse

def test_compute_mse_basic():
    assert compute_mse([1, 2, 3], [1, 2, 3]) == 0

def test_compute_mse_typical():
    assert round(compute_mse([1, 2, 3], [2, 3, 4]), 2) == 1.0

def test_compute_mse_mismatched_lengths():
    with pytest.raises(ValueError):
        compute_mse([1, 2, 3], [1, 2])
