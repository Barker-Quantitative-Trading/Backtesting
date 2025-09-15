from src.data.db import get_db_connection

def main():
    print("Testing DB connection...")
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")  # simple test query
        print("Connection Successful! Result:", cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print("Connection failed:", e)

if __name__ == "__main__":
    main()


# To run the code (you have to bee in root dir)
#python3 -m src.tests.test_db_conn
