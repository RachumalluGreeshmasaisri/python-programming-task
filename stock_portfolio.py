import os

def stock_portfolio_tracker():
    """
    Tracks stock portfolio value based on user input and hardcoded prices.
    """
    # Hardcoded dictionary for stock prices
    stock_prices = {"AAPL": 180.0, "TSLA": 250.0, "GOOGL": 150.0, "MSFT": 400.0}

    # Dictionary to store user's portfolio (stock: quantity)
    portfolio = {}
    total_investment = 0.0

    print("--- Stock Portfolio Tracker ---")
    print("Available stocks and prices:", stock_prices)

    # Get user input for stocks and quantity
    while True:
        stock_name = input("Enter stock ticker (e.g., AAPL) or 'done' to finish: ").strip().upper()
        if stock_name == 'DONE':
            break
        
        if stock_name in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {stock_name}: "))
                if quantity > 0:
                    portfolio[stock_name] = quantity
                else:
                    print("Quantity must be positive.")
            except ValueError:
                print("Invalid quantity. Please enter an integer.")
        else:
            print(f"Stock ticker '{stock_name}' not found in our list.")

    # Calculate total investment
    if not portfolio:
        print("No stocks in portfolio.")
        return

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = price * quantity
        total_investment += value
        print(f"{stock}: {quantity} shares * ${price:.2f}/share = ${value:.2f}")

    print(f"\n*Total Investment Value: ${total_investment:.2f}*")

    # Optional: Save results to a file
    save_option = input("Do you want to save the results to a text file? (yes/no): ").strip().lower()
    if save_option == 'yes':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary:\n")
            for stock, quantity in portfolio.items():
                f.write(f"{stock}: {quantity} shares\n")
            f.write(f"\nTotal Investment Value: ${total_investment:.2f}\n")
        print("Summary saved to portfolio_summary.txt")

if __name__ == "__main__":
    stock_portfolio_tracker()