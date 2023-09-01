import sqlite3
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