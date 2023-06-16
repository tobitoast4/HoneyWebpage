from database.database_connection import conn, cur


def create_table_product_category():
    cur.execute("""
        Create table IF NOT EXISTS product_category (
          product_category_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()