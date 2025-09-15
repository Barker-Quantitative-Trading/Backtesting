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

base_url = "https://api.tiingo.com"
load_dotenv()  # automatically finds .env in cwd
tokenHeader = os.getenv("TIINGO_TOKEN_HEADER")

"""
Takes symbol (str)
returns a dictionary of all the info tiingo has about that symbol
"""
def fetch_instrument(symbol: str) -> dict:

    endpoint = f"/tiingo/daily/{symbol}"
    url = f"{base_url}{endpoint}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {tokenHeader}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error fetching instrument {symbol}: {response.status_code}")
        print("Response text:", response.text[:200])
        return {}

    try:
        return response.json()
    except ValueError:
        print("Failed to decode JSON response for instrument:", symbol)
        return {}



""" 
Takes in a symbol (str), 
Start and end date (str) format: "year/month/day"
If only passed two parameters of symbol and start date end date will be set to none
    the will give you upto current date
Function returns data in json format
"""
def fetch_ohlcv(symbol: str, start_date: str, end_date: str = None) -> list:

    if(end_date):
        endpoint = f"/tiingo/daily/{symbol}/prices?startDate={start_date}&endDate={end_date}&"
    else:
        endpoint = f"/tiingo/daily/{symbol}/prices?startDate={start_date}&"

    url = f"{base_url}{endpoint}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {tokenHeader}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Error fetching instrument {symbol}: {response.status_code}")
        print("Response text:", response.text[:200])
        return {} 
    try:
        return(response.json())
    except ValueError:
        print("Failed to decode JSON response for instrument:", symbol)
        return{}