# Investment Portfolio Tracker 📈

## Project Overview

The **Investment Portfolio Tracker** is a Python-based application that helps users manage and analyze their stock investments.

Users can enter stock ticker symbols, buying prices, share quantities, and current market prices. The program calculates the total investment, current portfolio value, and percentage gain or loss for each stock and the overall portfolio.

It also automatically saves transaction summaries into a CSV file for future reference.

## Objectives

- To track multiple stock investments.
- To calculate the total invested amount.
- To determine the current market value of stocks.
- To calculate profit or loss for individual stocks.
- To calculate the overall portfolio performance.
- To store portfolio summaries in an external CSV file.

## Features

- **Stock Validation:** Validates ticker symbols using an S&P 500 companies dataset.
- **Multiple Stocks:** Allows users to enter multiple stock holdings.
- **Input Validation:** Prevents invalid prices, quantities, and ticker symbols.
- **Profit and Loss Calculation:** Calculates individual stock gains and losses.
- **Portfolio Summary:** Displays total investment, current value, and overall returns.
- **CSV Export:** Automatically saves portfolio details and transaction summaries.
- **Timestamp:** Records the date and time of each portfolio summary.

## Technologies Used

- Python 3
- CSV Module
- OS Module
- Datetime Module

## Project Structure

```text
Datheon_Python_Programming_Internship/
│
├── portfolio.py
├── sp500_companies.csv
├── portfolio_summary.csv
└── README.md
```

**File Description:**

- `portfolio.py` – Main Python application.
- `sp500_companies.csv` – Dataset containing S&P 500 company names and ticker symbols.
- `portfolio_summary.csv` – Automatically generated file containing portfolio transaction summaries.
- `README.md` – Project documentation.

## Dataset

The project uses an S&P 500 company dataset containing:

- Stock ticker symbols
- Company names
- Industry sectors
- Sub-industries
- Headquarters locations

**Dataset Source:**

[GitHub – S&P 500 Companies Dataset](https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv)

The dataset is used to validate stock ticker symbols and retrieve company names.

**Note:** Current stock prices are entered manually by the user. The dataset does not provide live stock market prices.

## Installation and Setup

### Step 1: Install Python

Install Python 3 or later on your computer.

### Step 2: Download the Project

Download or clone the project repository from GitHub.

### Step 3: Keep the Dataset Ready

Place `sp500_companies.csv` in the same folder as `portfolio.py`.

Make sure the CSV file contains the actual dataset, not Markdown code fences.

### Step 4: Run the Program

Open the terminal in the project folder and execute:

```bash
python portfolio.py
```

No external Python libraries are required.

## How to Use

1. Run the Python program.
2. Enter the number of different stocks you want to track.
3. Enter a valid stock ticker symbol.
4. Enter the buying price per share.
5. Enter the number of shares purchased.
6. Enter the current market price per share.
7. Repeat the process for other stocks.
8. View the individual stock and total portfolio summaries.
9. The program automatically saves the results to `portfolio_summary.csv`.

## Sample Input

```text
How many different stocks do you want to enter? 2

Enter details for stock 1
Enter stock ticker symbol: AAPL
Enter buying price per share: 150
Enter number of shares: 5
Enter current market price per share: 180

Enter details for stock 2
Enter stock ticker symbol: MSFT
Enter buying price per share: 300
Enter number of shares: 2
Enter current market price per share: 280
```

*The prices above are sample values used for testing.*

## Calculation Formulas

**1. Invested Amount**

Invested Amount = Buying Price × Quantity

**2. Current Market Value**

Current Value = Current Price × Quantity

**3. Gain or Loss**

Gain/Loss = Current Value − Invested Amount

**4. Gain or Loss Percentage**

Gain/Loss Percentage = (Gain/Loss ÷ Invested Amount) × 100

## Sample Output

```text
========== PORTFOLIO SUMMARY ==========

Stock: AAPL
Company: Apple Inc.
Quantity: 5
Buying Price: 150.0
Current Price: 180.0
Invested Amount: 750.0
Current Value: 900.0
Gain/Loss: 150.0
Gain/Loss Percentage: 20.0 %

Stock: MSFT
Company: Microsoft
Quantity: 2
Buying Price: 300.0
Current Price: 280.0
Invested Amount: 600.0
Current Value: 560.0
Gain/Loss: -40.0
Gain/Loss Percentage: -6.67 %

========== TOTAL PORTFOLIO ==========

Total Investment: 1350.0
Total Current Value: 1460.0
Total Gain/Loss: 110.0
Total Gain/Loss Percentage: 8.15 %

Portfolio report saved successfully!
```

## CSV Report

The program automatically creates `portfolio_summary.csv` to store:

- Date and time
- Stock ticker
- Company name
- Buying price
- Quantity
- Current price
- Invested amount
- Current value
- Gain or loss
- Gain or loss percentage

Each new execution appends another transaction summary to the CSV file.

## Python Concepts Used

- Functions
- Dictionaries
- Lists
- Loops
- Conditional statements
- Exception handling
- File handling
- CSV reading and writing
- Mathematical calculations
- Date and time handling

## Future Improvements

- Integrate a live stock market API to fetch current stock prices.
- Develop a graphical user interface using Tkinter or Streamlit.
- Add interactive portfolio performance charts.
- Support additional stock markets.
- Add historical investment tracking.

## Conclusion

The Investment Portfolio Tracker demonstrates how Python can be used to manage and analyze stock investments. It automates investment calculations, identifies profit and loss, validates stock symbols using a dataset, and stores transaction summaries in a CSV file.

This project helped develop practical skills in Python programming, data handling, file management, and financial calculations.

## Internship Information

**Internship:** Python Programming Internship  
**Organization:** Datheon  
**Batch:** 01  
**Project:** Investment Portfolio Tracker  
**Duration:** 4 Weeks

## Author

**Radhika Jejurkar**  
B.Sc. Data Science Student
