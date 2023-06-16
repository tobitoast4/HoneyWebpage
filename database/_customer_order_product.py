from database.database_connection import conn, cur


def create_table_customer_order_product():
    cur.execute("""
        Create table IF NOT EXISTS customer_order_product (
          customer_order_products_id INTEGER PRIMARY KEY,
          customer_order_id INT,
          product_id INT,
          amount INT,
          price_single REAL,
          FOREIGN KEY(customer_order_id) REFERENCES customer_order(order_id),
          FOREIGN KEY(product_id) REFERENCES product(product_id)
        );
    """)
    conn.commit()