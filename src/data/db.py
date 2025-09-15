# DB connection and communication
"""
db.py
Handles database connection and generic query execution.

The difficult part about this development is making sure that it works with the docker setup that will eventually live on the server
"""

def get_connection():
    """
    Open a connection to the database using environment variables.
    Returns a connection object.
    """
    pass

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