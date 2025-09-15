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
    """
    Ensure the symbol is valid (string, uppercase).
    """
    pass

def validate_timestamp(ts):
    """
    Ensure the timestamp is valid (datetime or string format).
    """
    pass

def validate_ohlcv(open_price, high, low, close, volume):
    """
    Validate OHLCV values (no negatives, logical consistency).
    """
    pass