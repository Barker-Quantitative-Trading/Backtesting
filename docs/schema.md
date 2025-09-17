# Market Data Database Schema

This the current plan for they database schema to allow backtesting and for an option of storing tick level data if needed.

---

## 1. assets Table

**Purpose:** Store metadata for financial assets (stocks, crypto, forex, etc.).

| Column     | Type       | Description                                           |
|------------|----------- |-------------------------------------------------------|
| id         | SERIAL PK  | Unique identifier                                     |
| symbol     | TEXT       | asset symbol (e.g., AAPL, BTC-USD)               |
| name       | TEXT       | Full name of the asset                           |
| type       | TEXT       | asset type (stock, crypto, forex, etc.)          |
| exchange   | TEXT       | Exchange code                                         |
| currency   | TEXT       | Denomination currency                                 |
| metadata   | JSONB      | Flexible storage for additional asset info       |

**Notes:**  
- `symbol` is unique.  
- `metadata` can store tick size, lot size, margin requirements, etc.  

---

## 2. Tick Data Table

**Purpose:** Store tick-level trades and quotes.

| Column        | Type         | Description                                       |
|---------------|------------- |---------------------------------------------------|
| id            | BIGSERIAL PK | Unique tick identifier                            |
| asset_id | INT FK       | References `assets.id`                       |
| ts            | TIMESTAMPTZ  | Timestamp of the tick                             |
| price         | NUMERIC      | Trade price                                       |
| volume        | NUMERIC      | Trade volume                                      |
| bid           | NUMERIC      | Current bid price                                 |
| ask           | NUMERIC      | Current ask price                                 |
| bid_size      | NUMERIC      | Size available at bid                             |
| ask_size      | NUMERIC      | Size available at ask                             |

**Indexes:**  
- `(asset_id, ts)` for efficient time-series queries  

---

## 3. candle Table

**Purpose:** Store aggregated price data (candles) at different intervals.

| Column       | Type         | Description                                       |
|------------- |--------------|---------------------------------------------------|
| id           | BIGSERIAL PK | Unique row identifier                             |
| asset_id| INT FK       | References `assets.id`                       |
| interval     | TEXT         | Resolution of the candle (1m, 5m, 1h, 1d, etc.)   |
| ts           | TIMESTAMPTZ  | Start time of the interval                        |
| open         | NUMERIC      | Opening price                                     |
| high         | NUMERIC      | Highest price in interval                         |
| low          | NUMERIC      | Lowest price in interval                          |
| close        | NUMERIC      | Closing price                                     |
| volume       | NUMERIC      | Total traded volume                               |
| adj_open     | NUMERIC      | Adjusted open price (splits/dividends)            |
| adj_high     | NUMERIC      | Adjusted high price                               |
| adj_low      | NUMERIC      | Adjusted low price                                |
| adj_close    | NUMERIC      | Adjusted close price                              |
| adj_volume   | NUMERIC      | Adjusted volume                                   |
| div_cash     | NUMERIC      | Dividend payout                                   |
| split_factor | NUMERIC      | Stock split factor                                |

**Indexes:**  
- `(asset_id, interval, ts)` for fast lookups  

**Notes:**  
- Adjusted columns are optional for intraday feeds without corporate actions.  
- Supports multiple intervals in the same table.  

---

## General Notes

- All foreign keys enforce referential integrity.  
- Use PostgreSQL comments for inline documentation (`COMMENT ON TABLE ...`).  
- Use migrations to track changes over time.  
- JSONB columns provide flexibility for additional attributes without schema changes.