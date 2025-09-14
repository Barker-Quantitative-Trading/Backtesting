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

conn = get_connection()
cur = conn.cursor()

print(conn.get_dsn_parameters())

cur.execute("SELECT id, symbol FROM instruments")

rows = cur.fetchall()
if not rows:
    print("nothing returned")

for row in rows:
    print(row)

cur.close()
conn.close()
