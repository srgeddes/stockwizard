import yfinance as yf
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests

# Function to fetch stock data
def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo")  # Last 3 month data
    return hist


# Function to plot the stock data in CLI
def plot_stock_data(ticker):
    hist = fetch_stock_data(ticker)
    
    plt.figure(figsize=(10, 5))
    plt.plot(hist.index, hist['Close'], label='Close Price')
    plt.title(f'Past 90 Days of {ticker}(NYSE)')
    plt.xlabel('Date')
    plt.ylabel('Price($USD)')
    plt.grid(True)
    plt.show()
