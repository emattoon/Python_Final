#(Database)
import sqlite3

def initialize_database():
    conn = sqlite3.connect("kitchen_inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ingredient TEXT UNIQUE,
            quantity INTEGER
        )
    """)
    conn.commit()
    conn.close()

def add_ingredient_to_db(ingredient, quantity):
    conn = sqlite3.connect("kitchen_inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO inventory (ingredient, quantity)
        VALUES (?, ?)
        ON CONFLICT(ingredient) DO UPDATE SET quantity = quantity + excluded.quantity
    """, (ingredient, quantity))
    conn.commit()
    conn.close()

def use_ingredient_in_db(ingredient, quantity):
    conn = sqlite3.connect("kitchen_inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE inventory
        SET quantity = quantity - ?
        WHERE ingredient = ? AND quantity >= ?
    """, (quantity, ingredient, quantity))
    conn.commit()
    conn.close()

def fetch_inventory_from_db():
    conn = sqlite3.connect("kitchen_inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ingredient, quantity FROM inventory")
    inventory = cursor.fetchall()
    conn.close()
    return inventory
