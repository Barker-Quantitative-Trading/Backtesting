import pytest
from src.data.db import get_db_connection, execute_query, execute_update

@pytest.fixture(scope="function")
def db_test_table():
    """
    Pytest fixture to set up and tear down a test table in the database.

    - Creates a 'pytest_test_table' before a test function runs.
    - Populates it with two initial records.
    - Yields control to the test function.
    - Drops the table after the test function completes.
    """
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Teardown from previous failed runs, just in case
            cur.execute("DROP TABLE IF EXISTS pytest_test_table;")
            # Setup: create table and insert initial data
            cur.execute("""
                CREATE TABLE pytest_test_table (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL
                );
            """)
            cur.execute("INSERT INTO pytest_test_table (name) VALUES (%s), (%s);", ('test_name_1', 'test_name_2'))
        conn.commit()
        
        yield # This is where the test runs

    finally:
        # Teardown: drop the table
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS pytest_test_table;")
        conn.commit()
        conn.close()

def test_execute_query_select_all(db_test_table):
    """
    Tests that execute_query can successfully fetch multiple records.
    """
    results = execute_query("SELECT * FROM pytest_test_table ORDER BY id;")
    
    assert len(results) == 2
    assert results[0]['name'] == 'test_name_1'
    assert results[1]['name'] == 'test_name_2'

def test_execute_update_insert(db_test_table):
    """
    Tests that execute_update can successfully insert a new record
    and returns the correct number of affected rows.
    """
    query = "INSERT INTO pytest_test_table (name) VALUES (%s);"
    params = ('new_test_name',)
    
    affected_rows = execute_update(query, params)
    
    assert affected_rows == 1
    
    # Verify the insert by querying the data back
    results = execute_query("SELECT name FROM pytest_test_table WHERE name = %s;", params)
    assert len(results) == 1
    assert results[0]['name'] == 'new_test_name'

def test_execute_update_with_invalid_sql_handles_error(capsys):
    """
    Tests that execute_update handles an exception gracefully by rolling back,
    returning 0, and printing an error.
    """
    # We don't need the fixture here as we are testing a failure case
    affected_rows = execute_update("INSERT INTO non_existent_table (name) VALUES ('fail');")
    
    assert affected_rows == 0
    
    # Check that an error message was printed to stderr/stdout
    captured = capsys.readouterr()
    assert "Error executing update" in captured.out
