"""
This Interface is what people outside of datalayer will use to talk to us.
If this grows a lot we have the availability to split things up for how it makes sense but for now this one class will work.

This will hopfully will sortof be a library for people to use.
The reason it only has gets and reads is because i'm trying to avoid anyone having to think about data.
So if the data does not exist create it sort of thing.
"""
import psycopg2

class DataAccess:

    """ Assets """
    def __init__():
        """Initialize connection (to be implemented)."""

    def list_assets():
        """Return all assets, optionally filtered by exchange or type."""

    def get_assets():
        """Fetch metadata for a single asset by symbol."""

    def search_assets():
        """Search assets by partial symbol or name."""


    """ candle """
    def get_candle():
        """Fetch candle data for a symbol within an optional date range."""
        """If no date range given it will return latest current candle data"""

    def get_bulk_candle():
        """Fetch candle data for multiple symbols at once."""
        """It is difficult to know if this one will really be needed"""

    def get_daily_returns():
        """Calculate daily returns from candle data for a symbol."""

    
    """ Utilities """
    def get_schema():
        """Return column names and types for a given table."""


   