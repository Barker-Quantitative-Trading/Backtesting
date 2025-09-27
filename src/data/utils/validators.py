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
from datetime import datetime

def validate_symbol(symbol):
    if type(symbol) != str: #checks the type
        return False
    else:
        return symbol.isupper()
    pass

def validate_timestamp(ts):
    #EXAMPLE: 2019-01-02T00:00:00.000Z
    #EXAMPLE 2: 2023-11-03T14:20:35+04:00
    if type(ts)!=str:
        return False
    try:
        dt = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as e:
        print(f"Invalid timestamp: {ts} -> {e}")
        return False
    if dt.year<1900: #make sure data is from 1900-present 
        return False
    elif dt.year>datetime.now().year:
        return False
    else:
        return True
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