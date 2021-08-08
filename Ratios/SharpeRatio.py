import pandas_datareader.data as web
import pandas as pd
import numpy as np

acceptableReturn = 0.02
investmentAmount = 100000

# defined as the Risk Free Rate, this is the amount the investor would have made from
# government funds and bonds, most of the time its = 0, or almost 0.
riskFreeRate = 0

# Method that returns timeseries data of a given security
# from two times..
# Both Start, End dates must be a datetime object
def retrieveData(Start, End, Ticker):
    modifiedStart = pd.to_datetime(Start)
    modifiedEnd = pd.to_datetime(End)
    stock = web.DataReader(Ticker,'yahoo',modifiedStart, modifiedEnd)
    return stock

# Retrieving the stockmarket data..
stock = retrieveData('2013-01-01','2020-10-01','FB')


# Sharpe Ratio Method
def sharpeRatio(stock):
    initialClosePrice = stock.iloc[0]['Adj Close']
    stock['Normalized Return'] = stock['Adj Close'] / initialClosePrice
    stock['Position Values'] = stock['Normalized Return'] * investmentAmount
    stock['Daily Return'] = stock['Position Values'].pct_change(1)
    mean = stock['Daily Return'].mean()
    standardDeviation = stock['Daily Return'].std()
    # Calculating the sharpe ratio..
    SR = (mean - riskFreeRate) / standardDeviation
    ASR = SR * (252**0.5)
    return ASR


print(sharpeRatio(stock))
