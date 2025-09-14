import psycopg2
from psycopg2.extras import execute_values
import requests
import json

# Fetch data from Tiingo
headers = {'Content-Type': 'application/json'}
requestResponse = requests.get(
    "https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=35943def70200e950c1dfa202bfcb2a4bb0b94a7",
    headers=headers
)
data = requestResponse.json()

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="market_data",
    user="postgres",
    password="devpass"
)
cur = conn.cursor()

# Map symbol to instrument_id
symbol_to_id = {"AAPL": 1}  # Make sure AAPL exists in instruments table

# Prepare rows for bulk insert
values = []
for bar in data:
    instrument_id = symbol_to_id["AAPL"]
    values.append((
        instrument_id,
        "1d",                    # interval
        bar["date"],             # ts
        bar.get("open"),
        bar.get("high"),
        bar.get("low"),
        bar.get("close"),
        bar.get("volume"),
        bar.get("adjOpen"),
        bar.get("adjHigh"),
        bar.get("adjLow"),
        bar.get("adjClose"),
        bar.get("adjVolume"),
        bar.get("divCash"),
        bar.get("splitFactor")
    ))

# Bulk insert (no ON CONFLICT)
sql = """
INSERT INTO ohlcv (
    instrument_id, interval, ts, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor
)
VALUES %s
"""

execute_values(cur, sql, values)
conn.commit()
cur.close()
conn.close()