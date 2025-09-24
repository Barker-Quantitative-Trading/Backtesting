"""
validators.py

Purpose:
--------
This module contains validation functions to ensure data integrity before
inserting or updating records in the database. This it to add an extra level between 
raw API responses and the database layer.

"""


"""
Helper functions to validate data before inserting into the DB.
These should return bool values if correct or not.
"""

def validate_symbol(symbol):
    if type(symbol) != str: #checks the type
        return False
    else:
        return symbol.isupper()
    pass

def validate_timestamp(ts):
    """
    Ensure the timestamp is valid (datetime or string format).
    """
    pass

def validate_candle(open_price, high, low, close, volume):
    if open_price < 0 or high < 0 or low < 0 or volume < 0 or close < 0: #checks if any of the variables are negative
        return False
    elif low > high: #confirms that low is lower than high
        return False
    elif close < low or close > high or open_price > high or open_price < low:
        return False
    else:
        return True
    pass