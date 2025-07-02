from flask import Flask, jsonify, request
from api import get_prices_for_tickers

app = Flask(__name__)

@app.route("/portfolio")
def get_portfolio():
    tickers_param = request.args.get("ticker")
    qty_param = request.args.get("qty")

    # Check if both parameters are provided
    if not tickers_param or not qty_param:
        return jsonify({"error": "Missing 'ticker' or 'qty' parameters"}), 400

    # Convert to lists
    tickers = tickers_param.upper().split(",")
    quantities = qty_param.split(",")

    # Validate input lengths match
    if len(tickers) != len(quantities):
        return jsonify({"error": "Number of tickers and quantities must match"}), 400

    # Build portfolio dictionary
    portfolio = {}
    for i in range(len(tickers)):
        try:
            portfolio[tickers[i]] = int(quantities[i])
        except ValueError:
            return jsonify({"error": f"Invalid quantity for {tickers[i]}"}), 400

    # Fetch live prices
    prices = get_prices_for_tickers(tickers)
    data = []

    # Build response
    for ticker in tickers:
        if prices[ticker] is None:
            continue

        price = float(prices[ticker])
        quantity = portfolio[ticker]
        total_value = price * quantity

        data.append({
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "total_value": total_value
        })

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
