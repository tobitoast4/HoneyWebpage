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


def get_all_customer_order_product() -> list:
    cur.execute("SELECT * FROM customer_order_product")
    customer_order_product_list = []
    for row in cur:
        customer_order_product_list.append(dict(zip([c[0] for c in cur.description], row)))
    return customer_order_product_list


def add_new_customer_order_product(customer_order_id, product_id, amount, price_single):
    cur.execute(f"""
        INSERT INTO customer_order_product (customer_order_products_id, customer_order_id, product_id, amount, price_single)
        VALUES (null, {customer_order_id}, {product_id}, {amount}, {price_single});
    """)
    conn.commit()


def get_customer_order_product_by_customer_order_id(customer_order_id):
    cur.execute(f"""
        SELECT *
        From customer_order_product
        WHERE customer_order_id={customer_order_id};
    """)

    order_product_list = []
    for row in cur:
        order_product_list.append(dict(zip([c[0] for c in cur.description], row)))
    return order_product_list
