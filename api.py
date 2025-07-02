import yfinance as yf

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.info["regularMarketPrice"]
        return price
    except Exception as e:
        print(f"[!] Failed to fetch price for {ticker}: {e}")
        return None

def get_prices_for_tickers(ticker_list):
    prices = {}
    for ticker in ticker_list:
        price = get_stock_price(ticker)
        if price is not None:
            prices[ticker] = price
        else:
            print(f"[!] No price found for {ticker}")
    return prices
