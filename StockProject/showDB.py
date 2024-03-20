import mysql.connector
import random

def get_stock_details_by_serial(host, username, password, database, serial_number):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute the query to retrieve details of the stock with the specified serial number
        cursor.execute("SELECT * FROM autodata WHERE `S.No.` = %s", (serial_number,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return rows
    except mysql.connector.Error as error:
        print("Error while retrieving stock details by serial number:", error)
        return []

def compare_stocks(stock_details, comparison_stock_details):
    # Implement your comparison logic here
    # For example, you can compare based on CMP, P/E ratio, market cap, etc.
    pass

# Provide your MySQL connection details
host = 'localhost'
username = 'root'
password = 'Asdqwe123@'
database = 'autodb'

# Prompt the user to enter the serial number of the stock
serial_number = int(input("Enter the serial number of the stock: "))

# Get the details of the specified stock by serial number
stock_details = get_stock_details_by_serial(host, username, password, database, serial_number)

if stock_details:
    print("Details for the entered stock:")
    for row in stock_details:
        print(row)  # Print each row of stock details
    
    # Select randomly a few other stocks from the database for comparison
    num_comparison_stocks = 2  # Adjust as needed
    connection = mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    all_serial_numbers_query = "SELECT `S.No.` FROM autodata"
    cursor.execute(all_serial_numbers_query)
    all_serial_numbers = [row[0] for row in cursor.fetchall()]
    comparison_serial_numbers = random.sample(all_serial_numbers, num_comparison_stocks)
    
    print("\nComparing with random stocks:")
    for comparison_serial_number in comparison_serial_numbers:
        comparison_stock_details = get_stock_details_by_serial(host, username, password, database, comparison_serial_number)
        if comparison_stock_details:
            print(f"\nComparison with stock having serial number {comparison_serial_number}:")
            for row in comparison_stock_details:
                print(row)  # Print each row of comparison stock details
            # Perform comparison
            compare_stocks(stock_details, comparison_stock_details)
        else:
            print(f"No details found for the comparison stock with serial number {comparison_serial_number}")
else:
    print(f"No details found for the stock with serial number {serial_number}")
