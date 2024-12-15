import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, period="5y", interval="1d"):
    """
    Fetch stock data for the given symbol using yfinance.
    Args:
        symbol (str): Stock ticker symbol (e.g., AAPL).
        period (str): Period for data (e.g., '5y', '1mo').
        interval (str): Data interval (e.g., '1d', '1h').
    Returns:
        pd.DataFrame or None: Stock data as a Pandas DataFrame, or None if failed.
        str or None: Error message if fetching fails, else None.
    """
    try:
        stock_data = yf.download(symbol, period=period, interval=interval)
        if stock_data.empty:
            return None, f"No data found for symbol: {symbol}"
        return stock_data, None
    except Exception as e:
        return None, str(e)
