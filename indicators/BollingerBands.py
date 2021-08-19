import datetime as dt
from yahoofinancials import YahooFinancials
import pandas as pd
import plotly.express as px



def fetchStockMarketData(ticker, days):
    """
    Gets the stockmarket data of a stock with the following parameters:
        * stock : the ticker
        * days : number of days ago
    """
    # Create the pandas dataframe..
    closePrices = pd.DataFrame()
    # Gets today's date and converts it to the YYYY-MM-DD format
    endDate = (dt.date.today()).strftime("%Y-%m-%d")
    # This gets the date from 1825 days ago by performing simple calculation and converts
    # The format to a YYYY-MM-DD format
    begDate = (dt.date.today() - dt.timedelta(days)).strftime("%Y-%m-%d")

    yahoo_financials = YahooFinancials(ticker)
    # Returns the data in json format
    jsonObj = yahoo_financials.get_historical_price_data(begDate, endDate, "daily")
    # Get all the json price fields..
    prices = jsonObj[ticker]["prices"]
    # creating a dataframe with json data, will make every field its own column
    pricesDataframe = pd.DataFrame(prices)
#    pricesDataframe.set_index("formatted_date", inplace=True)
    return (pricesDataframe)


def bollingerBands(stockData, n):
    def plotlyPlot(title, stock):
        """Method: Displays an interactive representation of given stock data in a
           line graph on your browser"""
        fig = px.line(title=title)

        fig.add_scatter(x=stock['formatted_date'], y=stock["BB_up"], name="BB_up")
        fig.add_scatter(x=stock['formatted_date'], y=stock["MA"], name="MA", fill="tonexty")
        fig.add_scatter(x=stock['formatted_date'], y=stock["BB_dn"], name="BB_dn", fill="tonexty")

        fig.show()



    """
    The standard deviation measures how spread out numbers are form an average value.
    The width the band displays the volatility, the wider the bands, the larger the volatility.
    """

    dataFrame = stockData.copy()
    dataFrame["MA"] = dataFrame["adjclose"].rolling(n).mean()
    dataFrame["BB_up"] = dataFrame["MA"] + 2 * dataFrame["MA"].rolling(n).std()
    dataFrame["BB_dn"] = dataFrame["MA"] - 2 * dataFrame["MA"].rolling(n).std()
    dataFrame["BB_range"] = dataFrame["BB_up"] - dataFrame["BB_dn"]
    dataFrame.dropna(inplace=True)

    plotlyPlot("BolingerBands" ,dataFrame[["formatted_date","MA", "BB_up", "BB_dn"]] )
    return dataFrame


stockData = fetchStockMarketData("AAPL" , 1820)
bollingerBands(stockData , 20)
