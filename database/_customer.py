from database.database_connection import conn, cur
from user import User


def create_table_customer():
    cur.execute("""
        Create table IF NOT EXISTS customer (
          customer_id INTEGER PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255) UNIQUE,
          password VARCHAR(255),
          phone_number VARCHAR(255),
          default_address_id INTEGER,
          FOREIGN KEY(default_address_id) REFERENCES address(address_id)
        );
    """)
    conn.commit()


def get_all_customers() -> list:
    cur.execute("SELECT * FROM customer")
    customer_list = []
    for row in cur:
        customer_list.append(dict(zip([c[0] for c in cur.description], row)))
    return customer_list


def add_new_customer(firstname, lastname, email_address, password, phone_number, default_address_id):
    cur.execute(f"""
        INSERT INTO customer (customer_id, firstname, lastname, email_address, password, phone_number, default_address_id)
        VALUES (null, "{firstname}", "{lastname}", "{email_address}", "{password}", "{phone_number}", {default_address_id});
    """)
    conn.commit()


def get_customer_by_id(customer_id):
    cur.execute(f"""
        SELECT *
        FROM customer
        WHERE customer_id="{customer_id}";
    """)
    customers = []
    for row in cur:
        customers.append(dict(zip([c[0] for c in cur.description], row)))
    if len(customers) == 0:
        return None
    c = customers[0]
    return User(c["customer_id"], c["firstname"], c["lastname"], c["email_address"],
                c["password"], c["phone_number"], c["default_address_id"])


def get_customer_by_email(email_address):
    cur.execute(f"""
        SELECT *
        FROM customer
        WHERE email_address="{email_address}";
    """)
    customers = []
    for row in cur:
        customers.append(dict(zip([c[0] for c in cur.description], row)))
    if len(customers) == 0:
        return None
    c = customers[0]
    return User(c["customer_id"], c["firstname"], c["lastname"], c["email_address"],
                c["password"], c["phone_number"], c["default_address_id"])


# def get_customer_with_address_by_id(customer_id):
#     cur.execute(f"""
#         SELECT *
#         FROM customer
#         LEFT OUTER JOIN address
#         ON customer.default_address_id = address.address_id
#         WHERE customer_id="{customer_id}";
#     """)
#     customers = []
#     for row in cur:
#         customers.append(dict(zip([c[0] for c in cur.description], row)))
#     return customers
