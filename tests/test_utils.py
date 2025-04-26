import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import normalize

def test_normalize_basic():
    assert normalize(10, 5, 5) == 1.0


def test_normalize_empty_list():
    with pytest.raises(ValueError):
        normalize(10, 10, 0)

