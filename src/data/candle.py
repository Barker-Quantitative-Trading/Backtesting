#CRUD file for candle table
"""
candle.py
Manages candle (price/time-series) data.
"""
from src.data.db import execute_query, execute_update

def insert_candle(symbol, timestamp, open_price, high, low, close, volume):
    """
    Insert candle data for a given symbol and timestamp.
    """
    query="INSERT INTO candle (ts, open, high, low, close, volume) VALUES ('%s, %s, %s, %s, %s, %s');"
    execute_query(query, (timestamp, open_price, high, low, close, volume))
    query="INSERT INTO assets (symbol) VALUES ('%s');"
    execute_query(query, (symbol))
    pass

def get_candle(symbol, start_date, end_date):
    """
    Fetch candle data for a symbol within a date range.
    """
    pass


def delete_candle(symbol, date):
    """
    Delete candle data for a given symbol and date.
    """
    pass