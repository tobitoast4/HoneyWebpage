from database.database_connection import conn, cur


def create_table_customer():
    cur.execute("""
        Create table IF NOT EXISTS customer (
          customer_id INTEGER PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255),
          phone_number VARCHAR(255),
          login_name VARCHAR(255),
          login_password VARCHAR(255),
          default_address_id INTEGER,
          FOREIGN KEY(default_address_id) REFERENCES address(address_id)
        );
    """)
    conn.commit()