import pandas as pd
import matplotlib.pyplot as plt
from api import get_prices_for_tickers

# Your current portfolio (ticker: quantity)
portfolio = {
    "AAPL": 10,
    "GOOGL": 3,
    "TSLA": 5
}

# Get live prices
tickers = list(portfolio.keys())
prices = get_prices_for_tickers(tickers)

# Build the portfolio data
data = []

for ticker in tickers:
    if prices[ticker] is None:
        print(f"Skipping {ticker}, no price data.")
        continue

    price = float(prices[ticker])
    quantity = portfolio[ticker]
    total_value = price * quantity

    data.append({
        "Ticker": ticker,
        "Quantity": quantity,
        "Price": price,
        "Total Value": total_value
    })

# Make a pandas DataFrame
df = pd.DataFrame(data)
df = pd.DataFrame(data)

# If there's no valid data, stop here
if df.empty:
    print("No valid stock data available. Exiting.")
    exit()


# Sort by highest value
df = df.sort_values(by="Total Value", ascending=False)

# Show it
print(df)

# Save to CSV
df.to_csv("portfolio.csv", index=False)

# Plot the portfolio
df.plot(kind="bar", x="Ticker", y="Total Value", legend=False)
plt.title("Portfolio Value by Ticker")
plt.xlabel("Stock")
plt.ylabel("Total Value ($)")
plt.tight_layout()
plt.show()
