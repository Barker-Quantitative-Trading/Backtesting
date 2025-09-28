from src.data.db import get_db_connection 
import pytest

def test_db_connection_and_query():
    """
    Tests that a database connection can be established and a simple query executed.
    This is an integration test and requires a running database.
    """
    conn = None
    try:
        conn = get_db_connection()
        assert conn is not None, "Database connection object should not be None."

        cur = conn.cursor()
        # Use an alias to make the test more robust with RealDictCursor
        cur.execute("SELECT 1 AS test_col;")
        result = cur.fetchone()

        assert result is not None, "Query should return a result."
        assert result['test_col'] == 1, "Query should return a dict with {'test_col': 1}"

    finally:
        # Ensure the connection is closed even if assertions fail
        if conn:
            conn.close()
