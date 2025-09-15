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
from dotenv import load_dotenv
import os

base_url = "https://api.tiingo.com/tiingo/daily"
load_dotenv()  # automatically finds .env in cwd
tokenHeader = os.getenv("TIINGO_TOKEN_HEADER")


def fetch_instrument(symbol: str) -> dict:
    """
    Fetch metadata for a single instrument from Tiingo.

    Args:
        symbol (str): The symbol of the instrument (e.g., 'AAPL').

    Returns:
        dict: Raw instrument data from the API that follows our current schema (if thats not possible than make a requset to have it modified)
    """
    pass


""" 
Takes in a symbol (str), 
Start and end date (str) format: "year/month/day"
If only passed two parameters of symbol and start date end date will be set to none
    the will give you upto current date
Function returns data in json format
"""
def fetch_ohlcv(symbol: str, start_date: str, end_date: str = None) -> list:

    if(end_date):
        endpoint = f"/{symbol}/prices?startDate={start_date}&endDate={end_date}&"
    else:
        endpoint = f"/{symbol}/prices?startDate={start_date}&"

    url = f"{base_url}{endpoint}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {tokenHeader}"
    }
    requestResponse = requests.get(url, headers=headers)
    return(requestResponse.json())