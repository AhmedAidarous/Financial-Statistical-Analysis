import pandas_datareader.data as pdr
import numpy as np
import datetime
import plotly.express as px


def plotlyPlot(title, stock):
    """Method: Displays an interactive representation of given stock data in a
       line graph on your browser"""
    fig = px.line(title=title)

    fig.add_scatter(x=stock['Date'], y=stock["OBV"], name="OBV" , fill="tozeroy")


    fig.show()


def OBV(stockFrame):
    """
    This is a method to calculate the On Balance Volume, which
    measures the momentum of volume trading, as an indicator of future
    asset price moves, so OBV theorem states that volume precedes price movement.

    """
    dataFrame = stockFrame.copy()
    dataFrame["dailyReturn"] = dataFrame["Adj Close"].pct_change(1)
    dataFrame["Direction"] = np.where(dataFrame["dailyReturn"] >= 0, 1 , -1)
    dataFrame["Direction"][0] = 0
    dataFrame["volumeAdj"] = dataFrame["Volume"] * dataFrame["Direction"]
    dataFrame["OBV"] = dataFrame["volumeAdj"].cumsum()

    dataFrame.dropna(inplace=True)
    return dataFrame[["Date","OBV" , "Close"]]


ticker = "AMZN"
ohlcv = pdr.get_data_yahoo(ticker , datetime.date.today() - datetime.timedelta(364), datetime.date.today())
ohlcv.reset_index(inplace=True)


stock = (OBV(ohlcv))
print(stock)

plotlyPlot("OBV Graph" , stock)


