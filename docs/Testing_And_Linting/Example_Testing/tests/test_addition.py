"""This is needed to describe the file"""
from functions.addition import add

def test_add_positive_numbers():
    """This is needed to describe the function"""
    assert add(2, 3) == 5
    assert add (0, 0) == 0

def test_add_strings():
    """This is needed to describe the function"""
    assert add("Hello ", "World") == "Hello World"
