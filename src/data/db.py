# DB connection and communication
import psycopg2
from psycopg2.extras import Json, execute_values

def get_connection():
    """Return a new connection to the database."""
    conn = psycopg2.connect(
        host="localhost",      # or your Docker service name
        port=5432,
        dbname="market_data",
        user="postgres",
        password="devpass"
    )
    return conn


import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_connection():
    """Return a new connection to the database."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "market_data"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        cursor_factory=RealDictCursor  # so fetch results as dicts
    )

def with_cursor(func):
    """
    Decorator to handle cursor/commit/close automatically.
    Lets you write DB functions without repeating boilerplate.
    """
    def wrapper(*args, **kwargs):
        conn = get_connection()
        try:
            with conn:
                with conn.cursor() as cur:
                    return func(cur, *args, **kwargs)
        finally:
            conn.close()
    return wrapper