#(Business Logic)
from db import add_ingredient_to_db, use_ingredient_in_db, fetch_inventory_from_db
from ui import display_inventory

def add_ingredient():
    ingredient = input("Enter the ingredient name: ").strip()
    quantity = int(input("Enter the quantity: "))
    add_ingredient_to_db(ingredient, quantity)
    print(f"Added {quantity} of {ingredient} to inventory.")

def use_ingredient():
    ingredient = input("Enter the ingredient name: ").strip()
    quantity = int(input("Enter the quantity to use: "))
    use_ingredient_in_db(ingredient, quantity)
    print(f"Used {quantity} of {ingredient} from inventory.")

def view_inventory():
    inventory = fetch_inventory_from_db()
    display_inventory(inventory)
