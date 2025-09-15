# DB connection and communication
"""
db.py
Handles database connection and generic query execution.

The difficult part about this development is making sure that it works with the docker setup that will eventually live on the server
"""
import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "market_data"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "devpass"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        cursor_factory=RealDictCursor  
    )
    return conn

def execute_query(query, params=None):
    """
    Execute a SELECT query and return results.
    Useful for reading data.
    """
    pass

def execute_update(query, params=None):
    """
    Execute INSERT/UPDATE/DELETE queries and commit changes.
    Useful for writing to the database.
    """
    pass