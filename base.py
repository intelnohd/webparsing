import sqlite3

LB_PATH = "labs.db"

def init_db():
    conn = sqlite3.connect(LB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert_labs(name):
    conn = sqlite3.connect(LB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def print_all_products():
    conn = sqlite3.connect(LB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    
    print("📦 Все товары в базе:")
    for row in rows:
        print(row)
    
    conn.close()
