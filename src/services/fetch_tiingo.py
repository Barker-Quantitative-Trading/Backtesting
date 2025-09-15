# Will be used to hold code relating to communication with tiingo
# ---------------------- fetch_tiingo.py ----------------------
"""
Purpose:
--------
This module handles all interactions with the Tiingo API. It is responsible
for fetching raw instrument metadata and historical OHLCV data, which
can later be validated and inserted into the database.
"""

import requests

def fetch_instrument(symbol: str) -> dict:
    """
    Fetch metadata for a single instrument from Tiingo.

    Args:
        symbol (str): The symbol of the instrument (e.g., 'AAPL').

    Returns:
        dict: Raw instrument data from the API that follows our current schema (if thats not possible than make a requset to have it modified)
    """
    pass

def fetch_ohlcv(symbol: str, start_date: str, end_date: str = None) -> list:
    """
    Fetch historical OHLCV data for an instrument from Tiingo.

    Args:
        symbol (str): The symbol of the instrument.
        start_date (str): The start date for historical data (YYYY-MM-DD).
        end_date (str, optional): The end date for historical data. Defaults to today.

    Returns:
        list: A list of OHLCV bars as dictionaries from the API.
    """
    pass