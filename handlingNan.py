import yfinance as yf
import datetime
import pandas as pd

stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "NVDA"]
start = datetime.datetime.today()-datetime.timedelta(365)
end = datetime.datetime.today()
cl_price = pd.DataFrame()
ohlcv = {}

for ticker in stocks: 
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
cl_price.dropna(axis = 0, how = 'any', inplace = True)

#print(cl_price.mean())
#print(cl_price.std())
#print(cl_price.median())
print(cl_price.describe())
print(cl_price.tail())

daily_return = cl_price.tail().pct_change()
print(daily_return)
print(daily_return.describe())