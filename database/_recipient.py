from database.database_connection import conn, cur


def create_table_recipient():
    cur.execute("""
        Create table IF NOT EXISTS recipient (
          recipient_id INTEGER PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255),
          phone_number VARCHAR(255),
          address_id INTEGER,
          FOREIGN KEY(address_id) REFERENCES address(address_id)
        );
    """)
    conn.commit()