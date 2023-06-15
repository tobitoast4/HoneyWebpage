import sqlite3 as sql

conn = sql.connect("shop.db", check_same_thread=False)
cur = conn.cursor()


def create_tables():
    cur.execute("""
        Create table IF NOT EXISTS customer (
          customer_id INT PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255),
          phone_number VARCHAR(255),
          login_name VARCHAR(255),
          login_password VARCHAR(255)
        );
        
        Create table IF NOT EXISTS recipient (
          recipient_id INT PRIMARY KEY,
          firstname VARCHAR(255),
          lastname VARCHAR(255),
          email_address VARCHAR(255),
          phone_number VARCHAR(255)
        );
        
        Create table IF NOT EXISTS product (
          product_id INT PRIMARY KEY,
          name VARCHAR(255),
          description VARCHAR(255),
          product_category_id INT,
          quantity_g INT,
          price REAL,
          FOREIGN KEY(product_category_id) REFERENCES product_category(product_category_id)
        );
        
        Create table IF NOT EXISTS address (
          address_id INT PRIMARY KEY,
          street VARCHAR(255),
          house_number INT,
          postal_code INT,
          city VARCHAR(255),
          country VARCHAR(255),
          state VARCHAR(255)
        );
        
        Create table IF NOT EXISTS customer_order (
          order_id INT PRIMARY KEY,
          order_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
          shipping_timestamp TIMESTAMP NOT NULL,
          delivery_cost REAL,
          customer_id INT,
          recipient_id INT,
          billing_address INT,
          delivery_address INT,
          order_state_id INT,
          payment_method_id INT,
          FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
          FOREIGN KEY(recipient_id) REFERENCES recipient(recipient_id),
          FOREIGN KEY(billing_address) REFERENCES address(address_id),
          FOREIGN KEY(delivery_address) REFERENCES address(address_id),
          FOREIGN KEY(order_state_id) REFERENCES order_state(order_state_id),
          FOREIGN KEY(payment_method_id) REFERENCES payment_method(payment_method_id)
        );
        
        Create table IF NOT EXISTS order_product (
          -- TODO: Add foreign key references
          order_product INT PRIMARY KEY,
          product_id INT,
          order_id INT,
          amount INT,
          price_single REAL
        );
        
        Create table IF NOT EXISTS product_category (
          product_category_id INT PRIMARY KEY,
          description VARCHAR(255)
        );
        
        Create table IF NOT EXISTS order_state (
          order_state_id INT PRIMARY KEY,
          description VARCHAR(255)
        );
        
        Create table IF NOT EXISTS payment_method (
          payment_method_id INT PRIMARY KEY,
          description VARCHAR(255)
        );
        

    """)