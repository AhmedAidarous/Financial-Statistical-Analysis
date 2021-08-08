# Importing Modules
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import datetime


# Get GSPC data..
# Method that returns timeseries data of a given security
# from two times..
# Both Start, End dates must be a datetime object
def retrieveData(Start, End, Ticker):
    modifiedStart = pd.to_datetime(Start)
    modifiedEnd = pd.to_datetime(End)
    stock = web.DataReader(Ticker,'yahoo',modifiedStart, modifiedEnd)
    return stock


def compoundAnnualGrowthRate(Df):
    df = Df
    df["Daily Return"] = Df["Adj Close"].pct_change(1)
    df["Cumulative Return"] = (1 + df["Daily Return"]).cumprod()
    n = len(df) / 252
    cagr = (df["Cumulative Return"][-1]) ** (1/n) - 1
    return cagr


def sortino(Data , riskFreeRate = 0.02):
    data = Data
    data['Daily Return'] = Data['Adj Close'].pct_change(1)
    negativeSTD = data[data["Daily Return"] < 0]["Daily Return"].std() * np.sqrt(252)
    sortino = (compoundAnnualGrowthRate(data) - riskFreeRate) / negativeSTD
    return sortino


dataFrame = retrieveData('01-01-2014','01-01-2019','TSLA')
print(sortino(dataFrame))




