from database.database_connection import conn, cur


def create_table_customer_order():
    cur.execute("""
        Create table IF NOT EXISTS customer_order (
          order_id INTEGER PRIMARY KEY,
          order_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          shipping_timestamp TIMESTAMP NOT NULL,
          delivery_cost REAL,
          customer_id INTEGER,
          recipient_id INTEGER,
          billing_address_id INTEGER,
          delivery_address_id INTEGER,
          order_state_id INTEGER,
          payment_method_id INTEGER,
          FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
          FOREIGN KEY(recipient_id) REFERENCES recipient(recipient_id),
          FOREIGN KEY(billing_address_id) REFERENCES address(address_id),
          FOREIGN KEY(delivery_address_id) REFERENCES address(address_id),
          FOREIGN KEY(order_state_id) REFERENCES order_state(order_state_id),
          FOREIGN KEY(payment_method_id) REFERENCES payment_method(payment_method_id)
        );
    """)
    conn.commit()