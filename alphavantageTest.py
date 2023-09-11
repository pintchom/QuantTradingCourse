from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import time

key = "0JP92YHXCU6Y6FYD"
ts =TimeSeries(key = key, output_format = 'pandas')
#data = ts.get_daily(symbol = "MSFT", outputsize="full")[0]
#print(data)

all_tickers = ["AAPL", "MSFT", "GOOG", "CSCO", "AMZN", "FB"]
close_prices = pd.DataFrame()
api_call_count = 0
for ticker in all_tickers:
    starttime = time.time()
    ts = TimeSeries(key = key, output_format='pandas')
    data = ts.get_intraday(symbol=ticker, interval = "1min", outputsize = "compact")[0]
    api_call_count += 1
    data.columns = ["open", "high", "low", "close", "volume"]
    close_prices[ticker] = data["close"]
    if api_call_count == 5:
        api_call_count = 0
        time.sleep(60)
print(close_prices)