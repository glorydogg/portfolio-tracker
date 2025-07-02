Portfolio Tracker (Flask API Version)

A Python-based stock portfolio tracker that pulls live stock prices using the Yahoo Finance API (yfinance), calculates your total holdings using Flask and Python, and returns clean JSON output via an API route. Also includes a CLI script to save to .csv and plot bar charts.

Features

Fetches real-time stock prices using Yahoo Finance (no API key required)

Accepts dynamic portfolio input via URL query parameters

Returns JSON-formatted portfolio value

CLI version includes pandas summary and bar chart output

Gracefully handles missing or failed API responses

Tech Stack

Python 3.x

Flask for API

pandas for CLI version

yfinance for real-time price data

matplotlib (optional, for CLI visualizations)

Installation

pip install flask yfinance pandas matplotlib

Usage

Web API:

Run the Flask server:

python app.py

Then visit:

http://127.0.0.1:5000/portfolio?ticker=AAPL,TSLA&qty=10,5

CLI Tracker:

Edit portfolio.py to define your stocks:

portfolio = {
  "AAPL": 10,
  "GOOGL": 3,
  "TSLA": 5
}

Then run:

python portfolio.py

Future Improvements



Example Output

JSON Output:

[
  {
    "ticker": "AAPL",
    "quantity": 10,
    "price": 192.45,
    "total_value": 1924.50
  },
  {
    "ticker": "TSLA",
    "quantity": 5,
    "price": 285.10,
    "total_value": 1425.50
  }
]

CLI Output:

Ticker  Quantity   Price  Total Value
AAPL    10         192.45   1924.50
GOOGL   3          2845.00  8535.00
TSLA    5          245.00   1225.00

Author

Built by Kanan Dimanche. GitHub: glorydogg
