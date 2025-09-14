# fetch_insert.py
import requests
from connect_db import get_connection
from psycopg2.extras import execute_values, Json
from datetime import datetime

# Fetch data from Tiingo
headers = {'Content-Type': 'application/json'}
api_url = "https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=35943def70200e950c1dfa202bfcb2a4bb0b94a7"
response = requests.get(api_url, headers=headers)
data = response.json()

# Connect to Database
conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT current_database(), inet_server_addr(), inet_server_port();")
print(cur.fetchone())

# Ensure the instrument exists
symbol = "AAPL"
cur.execute("SELECT id FROM instruments WHERE symbol = %s", (symbol,))
row = cur.fetchone()
if row is None:
    cur.execute("""
        INSERT INTO instruments (symbol, name, type, exchange, currency, metadata)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (symbol, "Apple Inc.", "stock", "NASDAQ", "USD", Json({"sector": "Technology"})))
    instrument_id = cur.fetchone()[0]
else:
    instrument_id = row[0]

# Prepare OHLCV rows
values = []
for bar in data:
    ts = datetime.fromisoformat(bar["date"].replace("Z", "+00:00")) 
    values.append((
        instrument_id,
        bar.get("interval", "1d"),
        ts,
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

# Bulk insert OHLCV
sql = """
INSERT INTO ohlcv (
    instrument_id, interval, ts, open, high, low, close, volume,
    adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor
) VALUES %s
"""
print(values[:3])
try:
    execute_values(cur, sql, values)
except Exception as e:
    print("insert error:", e)
# Commit and close
conn.commit()
cur.close()
conn.close()