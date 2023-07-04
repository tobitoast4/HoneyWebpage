from database.database_connection import conn, cur


def create_table_order_state():
    cur.execute("""
        Create table IF NOT EXISTS order_state (
          order_state_id INTEGER PRIMARY KEY,
          description VARCHAR(255)
        );
    """)
    conn.commit()


def get_all_order_states() -> list:
    cur.execute("SELECT * FROM order_state")
    order_state_list = []
    for row in cur:
        order_state_list.append(dict(zip([c[0] for c in cur.description], row)))
    return order_state_list


def add_new_order_state(description):
    cur.execute(f"""
        INSERT INTO order_state (order_state_id, description)
        VALUES (null, "{description}");
    """)
    conn.commit()


def insert_default_order_states():
    for cat in ["Bestellung aufgegeben", "Bezahlung ausstehend", "Wird nächstmöglich versendet", "Versandt"]:
        add_new_order_state(cat)