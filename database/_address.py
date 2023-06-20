from database.database_connection import conn, cur


def create_table_address():
    cur.execute("""
        Create table IF NOT EXISTS address (
          address_id INTEGER PRIMARY KEY,
          street VARCHAR(255),
          house_number INTEGER,
          postal_code INTEGER,
          city VARCHAR(255),
          country VARCHAR(255),
          state VARCHAR(255)
        );
    """)
    conn.commit()


def add_new_address(street, house_number, postal_code, city, country, state) -> int:
    cur.execute("""
        SELECT MAX(address_id)
        From address;
    """)

    new_id = [row[0] for row in cur][0]
    if new_id is None:
        new_id = 0
    else:
        new_id += 1

    cur.execute(f"""
        INSERT INTO address (address_id, street, house_number, postal_code, city, country, state)
        VALUES ({new_id}, "{street}", {house_number}, {postal_code}, "{city}", "{country}", "{state}");
    """)
    conn.commit()

    return new_id

