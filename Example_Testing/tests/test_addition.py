import pytest
from Functions.addition import add

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add (0, 0) == 0

def test_add_strings():
    assert add("Hello ", "World") == "Hello World"
