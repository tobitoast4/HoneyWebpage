from database.database_connection import conn, cur


def create_table_payment_method():
    cur.execute("""
        Create table IF NOT EXISTS payment_method (
          payment_method_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()
