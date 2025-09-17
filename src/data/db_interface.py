"""
This Interface is what people outside of datalayer will use to talk to us.
If this grows a lot we have the availability to split things up for how it makes sense but for now this one class will work.

This will hopfully will sortof be a library for people to use.
The reason it only has gets and reads is because i'm trying to avoid anyone having to think about data.
So if the data does not exist create it sort of thing.
"""
import psycopg2

class Interface:

    """ Instruments """
    def __init__():
        """Initialize connection (to be implemented)."""

    def list_instruments():
        """Return all instruments, optionally filtered by exchange or type."""

    def get_instrument():
        """Fetch metadata for a single instrument by symbol."""

    def search_instruments():
        """Search instruments by partial symbol or name."""


    """ OHLCV """
    def get_ohlcv():
        """Fetch OHLCV data for a symbol within an optional date range."""

    def get_latest_price():
        """Return the most recent close price for a symbol."""

    def get_bulk_ohlcv():
        """Fetch OHLCV data for multiple symbols at once."""
        """It is difficult to know if this one will really be needed"""

    def get_daily_returns():
        """Calculate daily returns from OHLCV data for a symbol."""

    
    """ Utilities """
    def get_schema():
        """Return column names and types for a given table."""
        

    """ Trades """

    """
    These are things for future implementation if 
    we are able to get this information somhow
    """
    def get_trades():
        """Fetch raw trade-level data for a symbol."""

    def get_order_book():
        """"Fetch snapshot of order book at given depth."""

