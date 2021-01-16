# handler module

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd



tickers = ["AAPL", "MSFT"]
startDate = "2010-01-01"
endDate = "2016-12-31"

panel = data.DataReader('INPX', 'yahoo', startDate, endDate)
panel.to_frame().head(9)
