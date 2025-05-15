# main.py (Main Program)
from ui import display_menu, get_user_choice
from db import initialize_database
from business import add_ingredient, use_ingredient, view_inventory

if __name__ == "__main__":
    initialize_database()
    
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            add_ingredient()
        elif choice == "2":
            use_ingredient()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
