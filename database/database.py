from database._address import *
from database._customer import *
from database._customer_order import *
from database._customer_order_product import *
from database._order_state import *
from database._payment_method import *
from database._product import *
from database._product_category import *
from database._recipient import *


def get_amount_tables_in_db():
    cur.execute("""
        SELECT count(*) as amount
        FROM sqlite_master
        WHERE type = 'table' AND
              name != 'android_metadata' AND
              name != 'sqlite_sequence';
    """)
    result = []
    for row in cur:
        result.append(dict(zip([c[0] for c in cur.description], row)))
    return result[0]["amount"]


def create_tables():
    create_table_address()
    create_table_customer()
    create_table_customer_order()
    create_table_customer_order_product()
    create_table_order_state()
    create_table_payment_method()
    create_table_product()
    create_table_product_category()
    create_table_recipient()


def insert_default_values():
    insert_default_products()


if get_amount_tables_in_db() <= 0:
    create_tables()
    insert_default_values()
