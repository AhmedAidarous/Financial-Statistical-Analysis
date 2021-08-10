
def bollingerBands(stockData, n):
    def plotlyPlot(title, stock):
        """Method: Displays an interactive representation of given stock data in a
           line graph on your browser"""
        fig = px.line(title=title)

        fig.add_scatter(x=stock['Date'], y=stock["BB_up"], name="BB_up")
        fig.add_scatter(x=stock['Date'], y=stock["MA"], name="MA", fill="tonexty")
        fig.add_scatter(x=stock['Date'], y=stock["BB_dn"], name="BB_dn", fill="tonexty")

        fig.show()



    """
    The standard deviation measures how spread out numbers are form an average value.
    The width the band displays the volatility, the wider the bands, the larger the volatility.
    """

    dataFrame = stockData.copy()
    dataFrame["MA"] = dataFrame["Adj Close"].rolling(n).mean()
    dataFrame["BB_up"] = dataFrame["MA"] + 2 * dataFrame["MA"].rolling(n).std()
    dataFrame["BB_dn"] = dataFrame["MA"] - 2 * dataFrame["MA"].rolling(n).std()
    dataFrame["BB_range"] = dataFrame["BB_up"] - dataFrame["BB_dn"]
    dataFrame.dropna(inplace=True)

    plotlyPlot("BolingerBands" ,dataFrame[["Date","MA", "BB_up", "BB_dn"]] )
    return dataFrame
