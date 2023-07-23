import sqlite3 as sql

db_file = "./database/shop.db"

conn = sql.connect(db_file, check_same_thread=False)
cur = conn.cursor()
