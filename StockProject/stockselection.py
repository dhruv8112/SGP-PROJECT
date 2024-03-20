# Sample dataset (replace this with your actual dataset)
stock_data = {
    'AAPL': {'price': 150.0, 'strength': 8},
    'GOOGL': {'price': 2500.0, 'strength': 9},
    'AMZN': {'price': 3500.0, 'strength': 7},
    'MSFT': {'price': 300.0, 'strength': 6}
}

def input_stock_data():
    stock_name = input("Enter stock name: ").upper()
    price = float(input("Enter stock price: "))
    return {'name': stock_name, 'price': price}

def find_strong_stock():
    # Customize this function based on your criteria for a strong stock
    return max(stock_data, key=lambda x: stock_data[x]['strength'])

def replace_weak_stock(weak_stock):
    strong_stock = find_strong_stock()
    stock_data[weak_stock['name']] = stock_data[strong_stock].copy()
    print(f"Replaced {weak_stock['name']} with {strong_stock}")

def main():
    user_stock = input_stock_data()

    if user_stock['name'] in stock_data:
        if user_stock['price'] < stock_data[user_stock['name']]['price']:
            print(f"{user_stock['name']} is weaker than the current stock in the dataset.")
            replace_weak_stock(user_stock)
        else:
            print(f"{user_stock['name']} is stronger than the current stock in the dataset.")
    else:
        print(f"{user_stock['name']} not found in the dataset.")

if __name__ == "__main__":
    main()
