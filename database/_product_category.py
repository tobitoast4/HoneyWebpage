from database.database_connection import conn, cur


def create_table_product_category():
    cur.execute("""
        Create table IF NOT EXISTS product_category (
          product_category_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()


def get_all_product_categories() -> list:
    cur.execute("SELECT * FROM product_category")
    product_category_list = []
    for row in cur:
        product_category_list.append(dict(zip([c[0] for c in cur.description], row)))
    return product_category_list


def add_new_category(description):
    cur.execute(f"""
        INSERT INTO product_category (product_category_id, description)
        VALUES (null, "{description}");
    """)
    conn.commit()


def insert_default_product_categories():
    for cat in ["Honig (flüssig)", "Honig (zähflüssig)", "Bienenvolk", "Utensilien"]:
        add_new_category(cat)
