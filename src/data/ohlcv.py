#CRUD file for ohlcv table
"""
ohlcv.py
Manages OHLCV (price/time-series) data.
"""

def insert_ohlcv(symbol, timestamp, open_price, high, low, close, volume):
    """
    Insert OHLCV data for a given symbol and timestamp.
    """
    pass

def get_ohlcv(symbol, start_date, end_date):
    """
    Fetch OHLCV data for a symbol within a date range.
    """
    pass

def get_latest_price(symbol):
    """
    Return the most recent close price for a symbol.
    """
    pass

def delete_ohlcv(symbol, date):
    """
    Delete OHLCV data for a given symbol and date.
    """
    pass