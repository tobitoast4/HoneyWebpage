from database.database_connection import conn, cur


def create_table_product():
    cur.execute("""
        Create table IF NOT EXISTS product (
          product_id INTEGER PRIMARY KEY,
          name VARCHAR(255),
          description VARCHAR(255),
          product_category_id INTEGER,
          quantity_g INTEGER,
          price REAL,
          amount_in_stock INTEGER,
          FOREIGN KEY(product_category_id) REFERENCES product_category(product_category_id)
        );
    """)
    conn.commit()


def add_new_product(name, description, product_category_id, quantity_g, price, amount_in_stock):
    cur.execute(f"""
        INSERT INTO product (product_id, name, description, product_category_id, quantity_g, price, amount_in_stock)
        VALUES (null, "{name}", "{description}", {product_category_id}, {quantity_g}, {price}, {amount_in_stock});
    """)
    conn.commit()


def get_all_products() -> list:
    cur.execute("SELECT * FROM product")
    product_list = []
    for row in cur:
        product_list.append(dict(zip([c[0] for c in cur.description], row)))
    return product_list


def get_product_data_for_cart() -> list:
    cur.execute("SELECT product_id, name, price FROM product")
    product_list = []
    for row in cur:
        product_list.append(dict(zip([c[0] for c in cur.description], row)))
    return product_list


def get_one_product(product_id: int):
    cur.execute(f"SELECT * FROM product WHERE product_id={product_id}")
    product_list = []
    for row in cur:
        product_list.append(dict(zip([c[0] for c in cur.description], row)))
    return product_list


def insert_default_products():
    import json

    with open('./database/res/default_products.json') as f:
        products = json.load(f)

    for p in products:
        add_new_product(
            p["name"],
            p["description"],
            p["product_category_id"],
            p["quantity_g"],
            p["price"],
            p["amount_in_stock"]
        )


def get_highest_product_price():
    cur.execute("""
        SELECT MAX(price)
        From product;
    """)
    import math

    try:
        return math.ceil([row for row in cur][0][0])
    except:
        return 100
