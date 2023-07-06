from database.database_connection import conn, cur


def create_table_recipient():
    cur.execute("""
        Create table IF NOT EXISTS recipient (
          recipient_id INTEGER PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255),
          phone_number VARCHAR(255),
          address_id INTEGER,
          FOREIGN KEY(address_id) REFERENCES address(address_id)
        );
    """)
    conn.commit()


def add_new_recipient(firstname, lastname, email_address, phone_number, address_id) -> int:
    cur.execute("""
        SELECT MAX(recipient_id)
        From recipient;
    """)

    new_id = [row[0] for row in cur][0]
    if new_id is None:
        new_id = 0
    else:
        new_id += 1

    cur.execute(f"""
        INSERT INTO recipient (recipient_id, firstname, lastname, email_address, phone_number, address_id)
        VALUES ({new_id}, "{firstname}", "{lastname}", "{email_address}", "{phone_number}", {address_id});
    """)
    conn.commit()

    return new_id


def get_recipient_with_address_by_id(recipient_id):
    cur.execute(f"""
        SELECT *
        FROM recipient
        LEFT OUTER JOIN address
        ON recipient.address_id = address.address_id
        WHERE recipient_id="{recipient_id}";
    """)
    recipients = []
    for row in cur:
        recipients.append(dict(zip([c[0] for c in cur.description], row)))
    return recipients
