# Main function for user interaction
def main():
    try:
        # Establish a connection to the products.db database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        while True:
            # Display the menu
            print("\nWarehouse CLI Menu:")
            print("1. Display Items")
            print("2. Exit")

            choice = input("Please select an option: ")

            if choice == "1":
                # Call the display_items function to show product information
                display_items(cursor)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose a valid option.")

    except sqlite3.Error as e:
        print("SQLite error:", e)
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()