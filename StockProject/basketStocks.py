import mysql.connector

class Stock:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

def connect_to_database(host, username, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)
        return None

def view_available_stocks(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM stocks")
        stocks = []
        for (id, name, price) in cursor:
            stocks.append(Stock(id, name, price))
        return stocks
    except mysql.connector.Error as error:
        print("Error while fetching available stocks:", error)
        return []

def purchase_stock(connection, stock_id, quantity):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM stocks WHERE id = %s", (stock_id,))
        stock = cursor.fetchone()
        if stock:
            total_price = stock[2] * quantity
            print(f"Purchased {quantity} shares of {stock[1]} for ${total_price}")
        else:
            print("Stock not found.")
    except mysql.connector.Error as error:
        print("Error while purchasing stock:", error)

def main():
    host = 'localhost'
    username = 'root'
    password = 'Asdqwe123@'
    database = 'autodb'

    # Connect to the database
    connection = connect_to_database(host, username, password, database)
    if connection is None:
        return

    while True:
        print("\nMenu:")
        print("1. View Available Stocks")
        print("2. Purchase Stock")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            stocks = view_available_stocks(connection)
            print("Available Stocks:")
            for stock in stocks:
                print(f"{stock.id}. {stock.name} - ${stock.price}")
        elif choice == '2':
            stock_id = int(input("Enter the stock ID to purchase: "))
            quantity = int(input("Enter the quantity to purchase: "))
            purchase_stock(connection, stock_id, quantity)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
