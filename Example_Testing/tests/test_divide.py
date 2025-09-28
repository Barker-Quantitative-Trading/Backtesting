"""This is needed to describe the file"""
import pytest
from Example_Testing.Functions.divide import divide

def test_divide_normal():
    """This is needed to describe the function"""
    assert divide(10, 2) == 5

def test_divide_raises():
    """This is needed to describe the function"""
    with pytest.raises(ValueError):
        divide(10, 0)
