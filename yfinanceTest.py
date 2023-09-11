import yfinance as yf
import datetime
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]
start = datetime.datetime.today()-datetime.timedelta(365)
end = datetime.datetime.today()
cl_price = pd.DataFrame()
ohlcv = {}

for ticker in stocks: 
    cl_price[ticker] = yf.download(ticker, start = start,end=end)["Adj Close"]
for ticker in stocks: 
    ohlcv[ticker] = yf.download(ticker, start = start,end=end)["Adj Close"]


#0JP92YHXCU6Y6FYD