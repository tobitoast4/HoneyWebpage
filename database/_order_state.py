from database.database_connection import conn, cur


def create_table_order_state():
    cur.execute("""
        Create table IF NOT EXISTS order_state (
          order_state_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()