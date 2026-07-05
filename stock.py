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
