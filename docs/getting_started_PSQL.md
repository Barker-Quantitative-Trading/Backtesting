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

-- 1. Create assets table
CREATE TABLE assets (
    id SERIAL PRIMARY KEY,
    symbol TEXT NOT NULL UNIQUE,
    name TEXT,
    type TEXT,
    exchange TEXT,
    currency TEXT,
    metadata JSONB
);

COMMENT ON TABLE assets IS 'Stores metadata for financial assets';
COMMENT ON COLUMN assets.symbol IS 'asset symbol (e.g., AAPL, BTC-USD)';
COMMENT ON COLUMN assets.metadata IS 'Flexible JSONB for additional info like tick size, lot size';

-- 2. Ticks table
CREATE TABLE ticks (
    id BIGSERIAL PRIMARY KEY,
    asset_id INT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    ts TIMESTAMPTZ NOT NULL,
    price NUMERIC(18,8),
    volume NUMERIC(18,8),
    bid NUMERIC(18,8),
    ask NUMERIC(18,8),
    bid_size NUMERIC(18,8),
    ask_size NUMERIC(18,8),
    source TEXT,
    UNIQUE (asset_id, ts, source)
);

COMMENT ON TABLE ticks IS 'Stores tick-level trades and quotes';
COMMENT ON COLUMN ticks.ts IS 'Timestamp of the tick event';
COMMENT ON COLUMN ticks.source IS 'Data source, e.g., Tiingo, Yahoo, Polygon';

-- Index for efficient time-series queries
CREATE INDEX idx_ticks_asset_ts ON ticks (asset_id, ts);

-- 3. Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    settings JSONB DEFAULT '{}' -- Flexible JSONB column for user preferences/settings
);

COMMENT ON TABLE users IS 'Stores user accounts and credentials';
COMMENT ON COLUMN users.settings IS 'Flexible JSONB column for user-specific settings and preferences';

-- 4. User Secrets table
CREATE TABLE user_secrets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    key_name TEXT NOT NULL, 
    encrypted_value TEXT NOT NULL, 
    UNIQUE (user_id, key_name) -- A user can only have one secret per key_name
);

COMMENT ON TABLE user_secrets IS 'Stores encrypted API keys and other sensitive user-specific secrets.';
COMMENT ON COLUMN user_secrets.key_name IS 'A descriptive name for the secret (e.g., "tiingo_api_key").';
COMMENT ON COLUMN user_secrets.encrypted_value IS 'The encrypted value of the secret.';

CREATE INDEX idx_user_secrets_user_id ON user_secrets (user_id);

-- 4. Posts table
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    username TEXT NOT NULL,
    text TEXT NOT NULL,
    strategy TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE posts IS 'Stores user-created posts, potentially related to strategies or market discussion.';
COMMENT ON COLUMN posts.strategy IS 'Optional link to a specific trading strategy.';

-- Index for retrieving posts by user
CREATE INDEX idx_posts_user_id ON posts (user_id);


-- 5. candle table
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

COMMENT ON TABLE candle IS 'Stores candle bars for assets';
COMMENT ON COLUMN candle.ts IS 'Timestamp of the candle bar';
COMMENT ON COLUMN candle.source IS 'Data source, e.g., Tiingo, Yahoo, Polygon';

-- Index for efficient time-series queries
CREATE INDEX idx_candle_asset_interval_ts ON candle (asset_id, interval, ts);

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