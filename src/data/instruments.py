#CRUD file for instruments table
"""
instruments.py
CRUD operations for instruments (tickers, metadata).
"""

def create_instrument(symbol, name, type, exchange, currency):
    """
    Insert a new instrument into the database.
    """
    pass

def get_instrument_by_symbol(symbol):
    """
    Retrieve instrument metadata by symbol (e.g. AAPL).
    """
    pass

def list_instruments():
    """
    Return all instruments stored in the database.
    """
    pass

def delete_instrument(symbol):
    """
    Delete an instrument by symbol.
    """
    pass