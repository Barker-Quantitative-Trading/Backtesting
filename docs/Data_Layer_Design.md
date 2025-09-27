### JSON Junkies

### Data Handling — Software Design Document

**Name:** Collin Worth\
**Date Created:** 2025-09-19\
**Date Last Updated:** 2025-09-25

---

## Summary

- [1 Introduction](#1-introduction)
- [2 System Overview](#2-system-overview)
- [3 System Architecture](#3-system-architecture)
- [4 Data Design](#4-data-design)
- [5 Component Design](#5-component-design)
- [6 Requirements Matrix](#6-requirements-matrix)

---

## 1 Introduction

### 1.1 Purpose

This document describes the design for the Data Layer Backtesting System. It explains how historical market data is stored in PostgreSQL and how it will be accessed for testing trading strategies.

### 1.2 Scope

- Ingesting historical market data from providers (Tiingo to start).
- Normalizing and storing OHLCV (open, high, low, close, volume) time-series data.
- Future support for multiple timeframes (minute, hourly, daily).
- Querying the database through the DataAccess library for production.

### 1.3 Overview

The system is a PostgreSQL database that stores time-series data and can be queried by other layers in the backtesting system.

### 1.4 Reference Material

- Tiingo API docs
- PostgreSQL docs

### 1.5 Definitions

- **OHLCV** — Open, High, Low, Close, Volume
- **TS** — Time Series
- **API** — Application Programming Interface

---

## 2 System Overview

The system ingests historical market data, stores it in PostgreSQL, and makes it available for backtesting.

Flow:

- Data is collected and inserted into PostgreSQL automatically via ingestion scripts.
- Queries are run through the DataAccess library to retrieve data for analysis.
- If requested items do not exist, the backend will fetch and store them as needed.

---

## 3 System Architecture

### 3.1 Components

- **PostgreSQL Database** — stores OHLCV tables and metadata.
- **DataAccess Library** — interfaces with the database for querying and backtesting.



```
[Data Source] -> [Postgres DB] -> [DataAccess Library]
```

---

## 4 Data Design

### 4.1 Core Tables

**assets**

- `id` SERIAL PRIMARY KEY
- `symbol` TEXT NOT NULL UNIQUE
- `name` TEXT
- `type` TEXT
- `exchange` TEXT
- `currency` TEXT
- `metadata` JSONB

**candle** 

- `id` BIGSERIAL PRIMARY KEY
- `asset_id` INT NOT NULL REFERENCES assets(id) ON DELETE CASCADE
- `interval` TEXT NOT NULL DEFAULT '1d'
- `ts` TIMESTAMPTZ NOT NULL
- `open` NUMERIC(18,8)
- `high` NUMERIC(18,8)
- `low` NUMERIC(18,8)
- `close` NUMERIC(18,8)
- `volume` NUMERIC(18,8)
- `adj_open` NUMERIC(18,8)
- `adj_high` NUMERIC(18,8)
- `adj_low` NUMERIC(18,8)
- `adj_close` NUMERIC(18,8)
- `adj_volume` NUMERIC(18,8)
- `div_cash` NUMERIC(18,8)
- `split_factor` NUMERIC(18,8)
- `source` TEXT
- **Unique Constraint** (`asset_id`, `interval`, `ts`, `source`)

**ingest\_log**

- `id` SERIAL PRIMARY KEY
- `symbol` TEXT NOT NULL
- `timeframe` TEXT NOT NULL
- `start_ts` TIMESTAMPTZ NOT NULL
- `end_ts` TIMESTAMPTZ NOT NULL
- `status` TEXT NOT NULL
- `rows_inserted` INT NOT NULL
- `error_msg` TEXT
- `duration_ms` BIGINT

### 4.2 Timezones

- All timestamps stored in UTC.

### 4.3 Partitioning

- OHLCV tables can be partitioned by date range to improve query performance.

---

## 5 Component Design

**PostgreSQL Database**

- Holds all data in a normalized schema.
- Ensures consistency and supports SQL queries for analysis.

**Data Collection / Ingestion Scripts**

- Fetches data from Tiingo and inserts into Postgres automatically.
- Logs ingestion results into `ingest_log`.

---

## 6 Requirements Matrix

1. Store data from Tiingo → PostgreSQL tables
2. Support multiple timeframes → separate OHLCV tables
3. Query data → through DataAccess library
4. Track ingestion results → `ingest_log` table



