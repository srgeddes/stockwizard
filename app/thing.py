import argparse
import requests
from bs4 import BeautifulSoup


def get_stock_data(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    price = soup.find(
        "fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketPrice"}
    )
    change = soup.find(
        "fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketChange"}
    )
    percent_change = soup.find(
        "fin-streamer",
        {"data-symbol": ticker, "data-field": "regularMarketChangePercent"},
    )

    if price and change and percent_change:
        print(f"Stock: {ticker}")
        print(f"Price: ${price.text}")
        print(f"Change: {change.text}")
        print(f"Percent Change: {percent_change.text}")
    else:
        print(f"Could not find data for {ticker}")


def main():
    parser = argparse.ArgumentParser(description="Get stock data from Yahoo Finance")
    parser.add_argument("ticker", type=str, help="Stock ticker symbol")
    args = parser.parse_args()

    get_stock_data(args.ticker)


if __name__ == "__main__":
    main()
