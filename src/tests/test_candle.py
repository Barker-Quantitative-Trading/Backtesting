import pytest, psycopg2
from src.data.candle import insert_candle, get_candle, delete_candle
from src.data.db import get_db_connection

@pytest.fixture(scope="function")
def candle():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS candle")
            cur.execute("""
            CREATE TABLE candle (
                id BIGSERIAL PRIMARY KEY,
                asset_id INT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
                interval TEXT NOT NULL DEFAULT '1d',
                ts TIMESTAMPTZ NOT NULL,
                open NUMERIC(18,8),
                high NUMERIC(18,8),
                low NUMERIC(18,8),
                close NUMERIC(18,8),
                volume NUMERIC(18,8),
                adj_open NUMERIC(18,8),
                adj_high NUMERIC(18,8),
                adj_low NUMERIC(18,8),
                adj_close NUMERIC(18,8),
                adj_volume NUMERIC(18,8),
                div_cash NUMERIC(18,8),
                split_factor NUMERIC(18,8),
                source TEXT,
                UNIQUE (asset_id, interval, ts, source)
            );
            """) #CREATION OF ASSETS TABLE MUST HAPPEN AFTER THIS
        yield
    finally:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS candle")
        conn.commit()
        conn.close()

def test_candle(candle):
    #insert_candle(symbol, interval, timestamp, open_price, high, low, close, volume, adj_open, adj_high, adj_low, adj_close, adj_volume, div_cash, split_factor)
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            insert_candle(
                symbol='AAPL', #CANNOT ADD THE SYMBOL DIRECTLY, NEEDS ASSETS TABLE IN ORDER TO BE FIXED
                interval='1d',
                timestamp='2019-01-02T00:00:00.000Z',
                open_price=100.0,
                high=110.0,
                low=95.0,
                close=105.0,
                volume=1000000,
                adj_open=99.0,
                adj_high=109.0,
                adj_low=94.0,
                adj_close=104.0,
                adj_volume=990000,
                div_cash=0.0,
                split_factor=1.0
            )
            #get_candle(symbol, start_date, end_date)
            row = get_candle('AAPL', '2019-01-02T00:00:00.000Z', '2019-01-02T00:00:00.001Z')
            assert row is not None
            assert row[1] == 'AAPL'
            assert row[2] == '1d'

            #delete_candle(symbol, date)
            """ 
            This portion will use assertions using delete_candle
            """
    finally:
        conn.commit()
        conn.close()
