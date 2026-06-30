import sqlite3

conn = sqlite3.connect("optirank.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    address TEXT,
    prescription TEXT
)
""")

conn.commit()

def add_customer(name, phone, address, prescription):
    cursor.execute(
        "INSERT INTO customers (name, phone, address, prescription) VALUES (?, ?, ?, ?)",
        (name, phone, address, prescription)
    )
    conn.commit()

def get_customers():
    cursor.execute("SELECT * FROM customers")
    return cursor.fetchall()
cursor.execute("""
CREATE TABLE IF NOT EXISTS bills (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_no TEXT,
    customer_name TEXT,
    phone TEXT,
    frame_brand TEXT,
    frame_model TEXT,
    lens_brand TEXT,
    lens_type TEXT,
    frame_price INTEGER,
    lens_price INTEGER,
    discount INTEGER,
    total INTEGER,
    payment_mode TEXT,
    bill_date TEXT
)
""")
