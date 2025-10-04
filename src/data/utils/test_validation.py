from utils.validators import validate_symbol

def test_validate_symbol():
    """This is needed to describe the function"""
    assert validate_symbol("AAPL") is True