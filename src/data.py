import yfinance as yf
import pandas as pd
import os

def download_and_clean_data(tickers, start_date, end_date):
    """Downloads asset price data and cleans it."""
    raw = yf.download(tickers, start=start_date, end=end_date)
    prices = raw.xs("Close", axis=1, level=0)
    returns = prices.pct_change().dropna()

    os.makedirs("../reports/assets", exist_ok=True)
    os.makedirs("../data", exist_ok=True)
    prices.to_csv("../data/asset_prices.csv")
    returns.to_csv("../data/asset_returns_clean.csv")

    return prices, returns

def download_extra_data(tickers, start_date, end_date, prices):
    """Downloads extra data for stress testing."""
    raw = yf.download(tickers, start=start_date, end=end_date)
    extra = raw.xs("Close", axis=1, level=0)
    prices = pd.concat([prices, extra]).sort_index().drop_duplicates()
    return prices