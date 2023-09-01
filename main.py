import sqlite3

# Function to create the database and table and insert sample data
def create_and_populate_database():
    try:
        # Create a connection to the database (this will create the database file)
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        # Create a products table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                category TEXT,
                price REAL
            )
        ''')

        # Insert sample data into the products table
        sample_data = [
            (1, "Product 1", "Electronics", 499.99),
            (2, "Product 2", "Clothing", 29.99),
            (3, "Product 3", "Home & Garden", 149.99)
        ]

        cursor.executemany('INSERT INTO products (id, title, category, price) VALUES (?, ?, ?, ?)', sample_data)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Database 'products.db' has been created and populated with sample data.")

    except sqlite3.Error as e:
        print("SQLite error:", e)

# Function to display all product items from the database
def display_items(cursor):
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if not products:
        print("No products found in the database.")
    else:
        print("Product List:")
        for product in products:
            print(f"ID: {product[0]}, Title: {product[1]}, Category: {product[2]}, Price: {product[3]} USD")

# Main function for user interaction
def main():
    # Create and populate the database if it doesn't exist
    create_and_populate_database()

    try:
        # Establish a connection to the products.db database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        while True:
            # Display the menu
            print("\nWarehouse CLI Menu:")
            print("1. Display Items")
            print("2. Exit")

            choice = input("Please select an option: ")  # Get user input for choice

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

