def ATR(stockData , ticker, n):
    """
    Functions to calculate True Range and Average True Range

    Definition: The Average True Range is the difference between
    the high and low prices on any given day, it reveals information
    about how volatile a stock is.

    Large ranges indicate high volatility and small ranges indicate low volatility.
    The range is measured the same way for options and commodities.

    """
    start = dt.datetime(2020, 1, 1)
    data = pdr.get_data_yahoo(ticker, start)

    high_low = data['High'] - data['Low']
    high_close = np.abs(data['High'] - data['Close'].shift())
    low_close = np.abs(data['Low'] - data['Close'].shift())

    ranges = pd.concat([high_low, high_close, low_close], axis=1)
    true_range = np.max(ranges, axis=1)

    atr = true_range.rolling(n).sum() / n


    # Returns the Average True Range dataframe / with the dates.
    return atr


