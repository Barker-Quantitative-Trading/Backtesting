#CRUD file for candle table
"""
candle.py
Manages candle (price/time-series) data.
"""
from src.data.db import execute_query, execute_update

def insert_candle(symbol, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor): #add the remaining columns from table
    """
    Insert candle data for a given symbol and timestamp.
    """
    query="""
    SELECT id, asset_id, symbol
    FROM candle
    INNER JOIN assets ON candle.asset_id = assets.id;
    """
    execute_update(query)
    query="""
    INSERT INTO candle (symbol, interval, ts, open, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    execute_update(query, (symbol, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor))
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