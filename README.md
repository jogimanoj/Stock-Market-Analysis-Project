# Stock-Market-Analysis-Project
#Stock Market Analysis Project downloads historical stock prices, computes summary statistics, and generates CSV reports and plots for quick exploratory analysis.
#Stock Market Analysis Project is a reproducible Python toolkit that downloads historical prices for configurable tickers and date ranges, cleans and aggregates the data, and computes summary statistics and common technical indicators. It outputs a combined stock_data.csv, summary tables, and charts saved to results/ for quick exploratory analysis or backtesting. Install dependencies with pip install -r requirements.txt and run python stock_analysis.py to fetch data and generate outputs.


#code


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = "AAPL"

stock = yf.download(ticker, start="2023-01-01", end="2025-01-01")

stock['MA50'] = stock['Close'].rolling(window=50).mean()
stock['MA200'] = stock['Close'].rolling(window=200).mean()
stock['Daily Return'] = stock['Close'].pct_change()

print("Stock:", ticker)
print("Volatility:", stock['Daily Return'].std())

stock.to_csv("stock_data.csv")

plt.figure(figsize=(12,6))
plt.plot(stock['Close'])
plt.title(f"{ticker} Closing Price")
plt.show()
