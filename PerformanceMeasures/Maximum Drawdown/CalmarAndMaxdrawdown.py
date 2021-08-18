import pandas_datareader.data as pdr
import numpy as np
import datetime

# Retrieve historic data from required stocks..
ticker = "AAPL"

# Ensure the data is daily
Snp = pdr.get_data_yahoo(ticker , datetime.date.today() - datetime.timedelta(1825) , datetime.date.today())



def CAGR(dataFrame):
    dataFrame["DailyReturn"] = dataFrame["Adj Close"].pct_change()
    dataFrame["CumulativeReturn"] = (1 + dataFrame["DailyReturn"]).cumprod()

    # Getting the number of years given daily data
    n = len(dataFrame) / 252
    CAGR = (dataFrame["CumulativeReturn"][-1]) ** (1/n) - 1

    return CAGR

  


def Maxdrawdown (dataFrame):
    dataFrame["DailyReturn"] = dataFrame["Adj Close"].pct_change()
    dataFrame["CumulativeReturn"] = (1 + dataFrame["DailyReturn"]).cumprod()
    dataFrame["CumulativeRollMax"] = dataFrame["CumulativeReturn"].cummax()

    dataFrame["DrawDown"] = dataFrame["CumulativeRollMax"] - dataFrame["CumulativeReturn"]
    dataFrame["DrawDown_PCT"] = dataFrame["DrawDown"].max()/dataFrame["CumulativeRollMax"]
    maximumDrawDown = dataFrame["DrawDown_PCT"].max()

    dataFrame["CumulativeReturn"].plot()
    plt.show()

    return maximumDrawDown

def Calmar (dataFrame):
    calmar = CAGR(dataFrame) / Maxdrawdown(dataFrame)
    return calmar

  
  



