import pytest
from Functions.divide import divide

def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_raises():
    with pytest.raises(ValueError):
        divide(10, 0)