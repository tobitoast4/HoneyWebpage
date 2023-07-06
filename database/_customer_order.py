from database.database_connection import conn, cur


def create_table_customer_order():
    cur.execute("""
        Create table IF NOT EXISTS customer_order (
          order_id INTEGER PRIMARY KEY,
          order_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          shipping_timestamp TIMESTAMP,
          delivery_cost REAL,
          customer_id INTEGER,
          recipient_id INTEGER,             -- this contains recipient and address
          -- billing_address_id INTEGER,    -- will always be the customers address (may change in the future)
          order_state_id INTEGER,
          payment_method_id INTEGER,
          FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
          FOREIGN KEY(recipient_id) REFERENCES recipient(recipient_id),
          -- FOREIGN KEY(billing_address_id) REFERENCES address(address_id),
          FOREIGN KEY(order_state_id) REFERENCES order_state(order_state_id),
          FOREIGN KEY(payment_method_id) REFERENCES payment_method(payment_method_id)
        );
    """)
    conn.commit()


def add_new_customer_order(delivery_cost, customer_id, recipient_id, order_state_id, payment_method_id) -> int:
    cur.execute("""
        SELECT MAX(order_id)
        From customer_order;
    """)

    new_id = [row[0] for row in cur][0]
    if new_id is None:
        new_id = 0
    else:
        new_id += 1

    cur.execute(f"""
        INSERT INTO customer_order (order_id, shipping_timestamp, delivery_cost, customer_id, recipient_id, 
                                    order_state_id, payment_method_id)
        VALUES ({new_id}, NULL, {delivery_cost}, {customer_id}, {recipient_id}, {order_state_id}, {payment_method_id});
    """)
    conn.commit()

    return new_id


def get_customer_orders_by_customer_id(customer_id):
    cur.execute(f"""
        SELECT *, os.description as order_state_description, pm.description as payment_method_description
        From customer_order
        LEFT JOIN order_state os ON customer_order.order_state_id = os.order_state_id
        LEFT JOIN payment_method pm ON customer_order.payment_method_id = pm.payment_method_id
        WHERE customer_id={customer_id}
        ORDER BY order_timestamp DESC;
    """)

    order_list = []
    for row in cur:
        order_list.append(dict(zip([c[0] for c in cur.description], row)))
    return order_list
