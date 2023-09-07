import yfinance as yf

data = yf.download(
    tickers="AAPL",
    period = "6mo"
)
print(data)