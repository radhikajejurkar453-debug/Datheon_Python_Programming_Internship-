
import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_FILE = os.path.join(BASE_DIR, "sp500_companies.csv")

OUTPUT_FILE = os.path.join(
    os.path.expanduser("~"),
    "portfolio_summary.csv"
)


def load_tickers():
    with open(DATASET_FILE, "r", newline="", encoding="utf-8-sig") as file:
        lines = (
            line for line in file
            if not line.strip().startswith("```")
        )

        reader = csv.DictReader(lines)
        tickers = {}

        for row in reader:
            if not row.get("Symbol") or not row.get("Security"):
                continue

            symbol = row["Symbol"].strip().upper()
            company = row["Security"].strip()

            if symbol and company:
                tickers[symbol] = company

    if not tickers:
        raise ValueError("No valid stock tickers found in the dataset.")

    return tickers


def get_positive_float(message):
    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Please enter a value greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number.")


def get_positive_integer(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Please enter a whole number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")


def calculate_portfolio(portfolio):
    total_invested = 0
    total_market_value = 0

    print("\n========== PORTFOLIO SUMMARY ==========")

    for symbol, details in portfolio.items():

        invested = details["buy_price"] * details["quantity"]
        market_value = details["current_price"] * details["quantity"]

        gain_loss = market_value - invested
        gain_loss_percent = (gain_loss / invested) * 100

        total_invested += invested
        total_market_value += market_value

        print("\nStock:", symbol)
        print("Company:", details["company"])
        print("Quantity:", details["quantity"])
        print("Buying Price:", round(details["buy_price"], 2))
        print("Current Price:", round(details["current_price"], 2))
        print("Invested Amount:", round(invested, 2))
        print("Current Value:", round(market_value, 2))
        print("Gain/Loss:", round(gain_loss, 2))
        print("Gain/Loss Percentage:", round(gain_loss_percent, 2), "%")

    total_gain_loss = total_market_value - total_invested

    total_gain_loss_percent = (
        (total_gain_loss / total_invested) * 100
    )

    print("\n========== TOTAL PORTFOLIO ==========")
    print("Total Investment:", round(total_invested, 2))
    print("Total Current Value:", round(total_market_value, 2))
    print("Total Gain/Loss:", round(total_gain_loss, 2))
    print("Total Gain/Loss Percentage:",
          round(total_gain_loss_percent, 2), "%")

    return (
        total_invested,
        total_market_value,
        total_gain_loss,
        total_gain_loss_percent
    )


def save_to_csv(portfolio, totals):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fieldnames = [
        "Date and Time",
        "Type",
        "Ticker",
        "Company",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested Amount",
        "Current Value",
        "Gain/Loss",
        "Gain/Loss Percentage"
    ]

    rows = []

    for symbol, details in portfolio.items():

        invested = details["buy_price"] * details["quantity"]
        market_value = details["current_price"] * details["quantity"]

        gain_loss = market_value - invested
        gain_loss_percent = (gain_loss / invested) * 100

        rows.append({
            "Date and Time": timestamp,
            "Type": "Stock",
            "Ticker": symbol,
            "Company": details["company"],
            "Buy Price": round(details["buy_price"], 2),
            "Quantity": details["quantity"],
            "Current Price": round(details["current_price"], 2),
            "Invested Amount": round(invested, 2),
            "Current Value": round(market_value, 2),
            "Gain/Loss": round(gain_loss, 2),
            "Gain/Loss Percentage": round(gain_loss_percent, 2)
        })

    rows.append({
        "Date and Time": timestamp,
        "Type": "TOTAL",
        "Ticker": "",
        "Company": "",
        "Buy Price": "",
        "Quantity": "",
        "Current Price": "",
        "Invested Amount": round(totals[0], 2),
        "Current Value": round(totals[1], 2),
        "Gain/Loss": round(totals[2], 2),
        "Gain/Loss Percentage": round(totals[3], 2)
    })

    try:
        file_exists = (
            os.path.exists(OUTPUT_FILE)
            and os.path.getsize(OUTPUT_FILE) > 0
        )

        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8-sig") as file:

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerows(rows)

        print("\nPortfolio report saved successfully!")
        print("File location:", OUTPUT_FILE)

    except PermissionError:
        print("\nError: Close portfolio_summary.csv if it is open in Excel.")

    except OSError as error:
        print("\nUnable to save CSV file:", error)


def main():
    try:
        tickers = load_tickers()

    except FileNotFoundError:
        print("Error: sp500_companies.csv was not found.")
        print("Keep the dataset in the same folder as portfolio.py.")
        return

    except (KeyError, csv.Error, ValueError) as error:
        print("Error loading stock dataset:", error)
        return

    portfolio = {}

    print("======================================")
    print("       INVESTMENT PORTFOLIO TRACKER")
    print("======================================")

    number_of_stocks = get_positive_integer(
        "\nHow many different stocks do you want to enter? "
    )

    for i in range(number_of_stocks):

        print("\nEnter details for stock", i + 1)

        while True:
            symbol = input("Enter stock ticker symbol: ").strip().upper()

            if symbol not in tickers:
                print("Ticker not found in the S&P 500 dataset.")
                continue

            if symbol in portfolio:
                print("This stock has already been entered.")
                continue

            break

        company = tickers[symbol]

        print("Company:", company)

        buy_price = get_positive_float(
            "Enter buying price per share: "
        )

        quantity = get_positive_integer(
            "Enter number of shares: "
        )

        current_price = get_positive_float(
            "Enter current market price per share: "
        )

        portfolio[symbol] = {
            "company": company,
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price
        }

    totals = calculate_portfolio(portfolio)

    save_to_csv(portfolio, totals)

    print("\nThank you for using the Portfolio Tracker!")


if __name__ == "__main__":
    main()

