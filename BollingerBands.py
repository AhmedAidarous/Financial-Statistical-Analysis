def bollingerBands(stockData , n):
    """
    The standard deviation measures how spread out numbers are form an average value.
    The width the band displays the volatility, the wider the bands, the larger the volatility.
    """
    
    dataFrame = stockData.copy()
    dataFrame["MA"] = dataFrame["Adj Close"].rolling(n).mean()
    dataFrame["BB_up"] = dataFrame["MA"] + 2*dataFrame["MA"].rolling(n).std()
    dataFrame["BB_dn"] = dataFrame["MA"] - 2*dataFrame["MA"].rolling(n).std()
    dataFrame["BB_range"] = dataFrame["BB_up"] - dataFrame["BB_dn"]
    dataFrame.dropna(inplace=True)
    dataFrame[["MA" , "BB_up" , "BB_dn"]].plot()
    plt.show()
    return dataFrame
