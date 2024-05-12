import requests
import json
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def plot_stock_data(stock_data):
    dates = list(stock_data["Time Series (Daily)"].keys())[::-1]
    prices = [float(stock_data["Time Series (Daily)"][date]["4. close"]) for date in dates]
    plt.figure(figsize=(12, 6))
    plt.plot(dates, prices, color='blue', marker='o', linestyle='-')
    plt.title('Historical Stock Prices for AAPL')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(dates[::50], rotation=45)
    plt.grid(True)
    plt.show()

def main():
    symbol = "AAPL" 
    api_key = "XTEC75R20RIB13YG"  
    stock_data = fetch_stock_data(symbol, api_key)
    plot_stock_data(stock_data)

if __name__ == "__main__":
    main()