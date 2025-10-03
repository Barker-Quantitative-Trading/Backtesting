# Market Data Database Schema

This document describes the database schema used for storing market data, user information, and other application data. The schema is implemented code is in `getting_started_PSQL.md`.

---

## 1. assets Table

**Purpose:** Stores metadata for financial assets (stocks, crypto, forex, etc.).

| Column   | Type    | Constraints                  | Description                                        |
|----------|---------|------------------------------|----------------------------------------------------|
| id       | SERIAL  | PRIMARY KEY                  | Unique identifier for the asset.                   |
| symbol   | TEXT    | NOT NULL, UNIQUE             | Asset symbol (e.g., 'AAPL', 'BTC-USD').            |
| name     | TEXT    |                              | Full name of the asset.                            |
| type     | TEXT    |                              | Asset type (e.g., 'stock', 'crypto', 'forex').     |
| exchange | TEXT    |                              | Exchange where the asset is traded.                |
| currency | TEXT    |                              | Denomination currency.                             |
| metadata | JSONB   |                              | Flexible storage for additional info (e.g., tick size). |

**Notes:**  
- `symbol` is unique.  
- `metadata` can store tick size, lot size, margin requirements, etc.  

---

## 2. ticks Table

**Purpose:** Store tick-level trades and quotes.

| Column   | Type        | Constraints                               | Description                               |
|----------|-------------|-------------------------------------------|-------------------------------------------|
| id       | BIGSERIAL   | PRIMARY KEY                               | Unique tick identifier.                   |
| asset_id | INT         | NOT NULL, FK to `assets.id` ON DELETE CASCADE | References the asset.                     |
| ts       | TIMESTAMPTZ | NOT NULL                                  | Timestamp of the tick event.              |
| price    | NUMERIC     |                                           | Trade price.                              |
| volume   | NUMERIC     |                                           | Trade volume.                             |
| bid      | NUMERIC     |                                           | Current bid price.                        |
| ask      | NUMERIC     |                                           | Current ask price.                        |
| bid_size | NUMERIC     |                                           | Size available at bid.                    |
| ask_size | NUMERIC     |                                           | Size available at ask.                    |
| source   | TEXT        |                                           | Data source (e.g., 'Tiingo').  |

**Indexes:**  
- `(asset_id, ts, source)` for uniqueness and efficient time-series queries.

---

## 3. candle Table

**Purpose:** Stores aggregated price data (OHLCV candles) at different intervals.

| Column       | Type        | Constraints                               | Description                                     |
|--------------|-------------|-------------------------------------------|-------------------------------------------------|
| id           | BIGSERIAL   | PRIMARY KEY                               | Unique row identifier.                          |
| asset_id     | INT         | NOT NULL, FK to `assets.id` ON DELETE CASCADE | References the asset.                           |
| interval     | TEXT        | NOT NULL, DEFAULT '1d'                    | Resolution of the candle ('1m', '5m', '1d').    |
| ts           | TIMESTAMPTZ | NOT NULL                                  | Start time of the interval.                     |
| open         | NUMERIC     |                                           | Opening price.                                  |
| high         | NUMERIC     |                                           | Highest price in interval.                      |
| low          | NUMERIC     |                                           | Lowest price in interval.                       |
| close        | NUMERIC     |                                           | Closing price.                                  |
| volume       | NUMERIC     |                                           | Total traded volume.                            |
| adj_open     | NUMERIC     |                                           | Adjusted open price (for splits/dividends).     |
| adj_high     | NUMERIC     |                                           | Adjusted high price.                            |
| adj_low      | NUMERIC     |                                           | Adjusted low price.                             |
| adj_close    | NUMERIC     |                                           | Adjusted close price.                           |
| adj_volume   | NUMERIC     |                                           | Adjusted volume.                                |
| div_cash     | NUMERIC     |                                           | Dividend payout during the interval.            |
| split_factor | NUMERIC     |                                           | Stock split factor during the interval.         |
| source       | TEXT        |                                           | Data source (e.g., 'Tiingo').        |

**Indexes:**  
- `(asset_id, interval, ts, source)` for uniqueness and fast lookups.

---

## 4. users Table

**Purpose:** Stores user accounts and credentials.

| Column        | Type        | Constraints                               | Description                                      |
|---------------|-------------|-------------------------------------------|--------------------------------------------------|
| id            | UUID        | PRIMARY KEY, DEFAULT `gen_random_uuid()`  | Unique identifier for the user.                  |
| username      | TEXT        | NOT NULL, UNIQUE                          | User's login name.                               |
| email         | TEXT        | NOT NULL, UNIQUE                          | User's email address.                            |
| password_hash | TEXT        | NOT NULL                                  | Hashed password (never store plaintext).         |
| settings      | JSONB       | DEFAULT '{}'                              | Flexible JSONB for user-specific preferences.    |

---

## 5. user_secrets Table

**Purpose:** Stores encrypted API keys and other sensitive user-specific secrets.

| Column          | Type        | Constraints                               | Description                                      |
|-----------------|-------------|-------------------------------------------|--------------------------------------------------|
| id              | UUID        | PRIMARY KEY, DEFAULT `gen_random_uuid()`  | Unique identifier for the secret entry.          |
| user_id         | UUID        | NOT NULL, FK to `users.id` ON DELETE CASCADE | The user this secret belongs to.                 |
| key_name        | TEXT        | NOT NULL                                  | A descriptive name for the secret (e.g., 'tiingo_api_key'). |
| encrypted_value | TEXT        | NOT NULL                                  | The encrypted value of the secret.               |

**Indexes:**
- `(user_id, key_name)` for uniqueness.
- `(user_id)` for fast lookups.

---

## 6. posts Table

**Purpose:** Stores user-created posts to share stratagies.

| Column     | Type        | Constraints                               | Description                                      |
|------------|-------------|-------------------------------------------|--------------------------------------------------|
| id         | UUID        | PRIMARY KEY, DEFAULT `gen_random_uuid()`  | Unique identifier for the post.                  |
| user_id    | UUID        | NOT NULL, FK to `users.id` ON DELETE CASCADE | The user who created the post.                   |
| username   | TEXT        | NOT NULL                                  | The username of the creator (denormalized for speed). |
| text       | TEXT        | NOT NULL                                  | The content of the post.                         |
| strategy   | TEXT        |                                           | Optional link to a specific trading strategy.    |
| created_at | TIMESTAMPTZ | NOT NULL, DEFAULT `NOW()`                 | Timestamp of post creation.                      |

**Indexes:**
- `(user_id)` for retrieving all posts by a user.

---

## General Notes

 
- `ON DELETE CASCADE` is used to automatically clean up related data (e.g., deleting a user also deletes their posts and secrets).
- JSONB columns provide flexibility for additional attributes without schema changes.