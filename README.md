# Exercise: Warehouse Command-Line Interface

*Objective:*
Practice working with SQLite databases, creating a command-line interface (CLI), and retrieving data to display to users by building a Warehouse CLI that connects to a product database.

*Instructions:*

1. *Setup:*
   - Ensure you have the products.db SQLite database file with product data stored.
2. *Task:*
   - Write a Python script that establishes a connection to the products.db database.
   - Implement a function display_items(cursor) that queries and displays all product items from the database.
   - Create a main() function that runs a loop for user interaction. The loop should:
     - Display a menu with the following options:
       - Display Items
       - Exit
     - Prompt the user to select an option.
     - If the user selects "Display Items," call the display_items function to show the products.
     - If the user selects "Exit," break the loop and print "Goodbye!"
3. *Implementation:*
   - Start by importing the necessary libraries (e.g., sqlite3).
   - Establish a connection to the products.db SQLite database.
   - Define the display_items(cursor) function that queries the products table and displays product information.
   - Define the main() function that contains a loop for user interaction. Inside the loop, display the menu and perform the selected action based on user input.
   - Close the database connection when exiting the program.
   