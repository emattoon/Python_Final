#(User Interface)
def display_menu():
    print("\n--- Kitchen Inventory Menu ---")
    print("1. Add Ingredient")
    print("2. Use Ingredient")
    print("3. View Inventory")
    print("4. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def display_inventory(inventory):
    print("\n--- Kitchen Inventory ---")
    for item, qty in inventory:
        print(f"{item}: {qty}")
