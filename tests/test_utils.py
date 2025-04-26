import pytest
from src.utils import normalize

def test_normalize_basic():
    assert normalize(10, 5, 5) == 1.0

def test_normalize_zero_std():
    with pytest.raises(ValueError):
        normalize(10, 10, 0)
