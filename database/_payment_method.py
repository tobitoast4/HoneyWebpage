from database.database_connection import conn, cur


def create_table_payment_method():
    cur.execute("""
        Create table IF NOT EXISTS payment_method (
          payment_method_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()


def get_all_payment_methods() -> list:
    cur.execute("SELECT * FROM payment_method")
    payment_method_list = []
    for row in cur:
        payment_method_list.append(dict(zip([c[0] for c in cur.description], row)))
    return payment_method_list


def add_new_payment_method(description):
    cur.execute(f"""
        INSERT INTO payment_method (payment_method_id, description)
        VALUES (null, "{description}");
    """)
    conn.commit()


def insert_default_payment_methods():
    for cat in ["PayPal", "Kreditkarte", "Giropay", "Überweisung"]:
        add_new_payment_method(cat)

