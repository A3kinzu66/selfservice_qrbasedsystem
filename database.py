import sqlite3

DB = "orders.db"

def connect():
    return sqlite3.connect(DB)

def setup():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            token TEXT PRIMARY KEY,
            items TEXT,
            amount TEXT,
            status TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def add_order(token, items, amount):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO orders VALUES (?, ?, ?, ?)",
                (token, items, amount, "PENDING"))
    
    conn.commit()
    conn.close()

def set_ready(token):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("UPDATE orders SET status='READY' WHERE token=?", (token,))
    
    conn.commit()
    conn.close()

def set_picked(token):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("DELETE FROM orders WHERE token=?", (token,))
    
    conn.commit()
    conn.close()

def get_pending():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT token, items FROM orders WHERE status='PENDING'")
    rows = cur.fetchall()
    
    conn.close()
    return rows

def get_ready():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT token, items FROM orders WHERE status='READY'")
    rows = cur.fetchall()
    
    conn.close()
    return rows

setup()