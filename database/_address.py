from database.database_connection import conn, cur


def create_table_address():
    cur.execute("""
        Create table IF NOT EXISTS address (
          address_id INTEGER PRIMARY KEY,
          street VARCHAR(255),
          house_number INTEGER,
          postal_code INTEGER,
          city VARCHAR(255),
          country VARCHAR(255),
          state VARCHAR(255)
        );
    """)
    conn.commit()