# PostgreSQL Setup and Market Data Schema

This guide covers installing PostgreSQL, starting the server, connecting, creating the `market_data` database, implementing the schema, and basic commands.

---

## 1 Install PostgreSQL

| Platform      | Command / Notes |
|---------------|----------------|
| **Mac / Linux** | macOS: `brew install postgresql`<br>Linux (Ubuntu): `sudo apt install postgresql postgresql-contrib` |
| **Windows**     | Download and run installer from [PostgreSQL Download](https://www.postgresql.org/download/windows/). Follow installer steps and set a password for the `postgres` superuser. |

---

## 2 Start PostgreSQL Server

| Platform      | Command / Notes |
|---------------|----------------|
| **Mac / Linux** | macOS: `brew services start postgresql`<br>Linux: `sudo systemctl start postgresql` |
| **Windows**     | Start PostgreSQL service via **Services** app or launch **pgAdmin** GUI. |

---

## 3 Connect to PostgreSQL

| Platform      | Command / Notes |
|---------------|----------------|
| **Mac / Linux** | `psql postgres` (CLI, default database is `postgres`) |
| **Windows**     | Open **psql** from Start Menu or:<br>`"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres` |

---

## 4 Create the `market_data` Database

```sql
CREATE DATABASE market_data;



**Create Database**
CREATE DATABASE market_data;

**Connect to the database**
\c market_data;

-- 2. Create Instruments table
CREATE TABLE instruments (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    name TEXT,
    type TEXT,
    exchange TEXT,
    currency TEXT,
    metadata JSONB
);

COMMENT ON TABLE instruments IS 'Stores metadata for financial instruments';
COMMENT ON COLUMN instruments.symbol IS 'Instrument symbol (e.g., AAPL, BTC-USD)';
COMMENT ON COLUMN instruments.metadata IS 'Flexible JSONB for additional info like tick size, lot size';

-- 3. Create Tick Data table
CREATE TABLE ticks (
    id BIGSERIAL PRIMARY KEY,
    instrument_id INT NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
    ts TIMESTAMPTZ NOT NULL,
    price NUMERIC(18,8),
    volume NUMERIC(18,8),
    bid NUMERIC(18,8),
    ask NUMERIC(18,8),
    bid_size NUMERIC(18,8),
    ask_size NUMERIC(18,8)
);

-- Index for efficient time-series queries
CREATE INDEX idx_ticks_instrument_ts ON ticks (instrument_id, ts);

COMMENT ON TABLE ticks IS 'Stores tick-level trades and quotes';
COMMENT ON COLUMN ticks.ts IS 'Timestamp of the tick event';

-- 4. Create OHLCV table
CREATE TABLE ohlcv (
    id BIGSERIAL PRIMARY KEY,
    instrument_id INT NOT NULL REFERENCES instruments(id) ON DELETE CASCADE,
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
    split_factor NUMERIC(18,8)
);

-- Index for OHLCV queries
CREATE INDEX idx_ohlcv_instrument_interval_ts ON ohlcv (instrument_id, interval, ts);

COMMENT ON TABLE ohlcv IS 'Stores aggregated OHLCV data with adjustable intervals';
COMMENT ON COLUMN ohlcv.interval IS 'Resolution of the candle (1m, 5m, 1h, 1d)';
COMMENT ON COLUMN ohlcv.adj_close IS 'Close price adjusted for splits/dividends';

-- Done! You now have a flexible, well-documented schema.
```

### Basic PstgreSQL Commands

| Command              | Description                               |
|----------------------|-------------------------------------------|
| `\l`                 | List all databases                        |
| `\c database_name`   | Connect to a specific database            |
| `\dt`                | List all tables in the current database   |
| `\d table_name`      | Show schema/details of a table            |
| `\du`                | List all roles and users                  |
| `\dn`                | List all schemas                          |
| `\df`                | List functions                            |
| `\q`                 | Quit/exit `psql`                          |
| `\?`                 | Show help for `psql` commands             |
| `\x`                 | Toggle expanded output (pretty print)     |
| `SELECT version();`  | Show PostgreSQL version                   |
| `CREATE DATABASE db;`| Create a new database                     |
| `DROP DATABASE db;`  | Delete a database                         |
| `\password user`     | Change password for a user                |