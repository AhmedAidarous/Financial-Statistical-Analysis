def MACD(openhighlowclosevolume , a , b , c):
  
    stockFrame = openhighlowclosevolume.copy()
    stockFrame["MA_Fast"] = stockFrame["Adj Close"].ewm(span=a, min_periods=a).mean()
    stockFrame["MA_Slow"] = stockFrame["Adj Close"].ewm(span=b, min_periods=b).mean()
    stockFrame["MACD"] = stockFrame["MA_Fast"] - stockFrame["MA_Slow"]
    stockFrame["Signal"] = stockFrame["MACD"].ewm(span=c , min_periods=c).mean()
    stockFrame.dropna(inplace=True)
    return stockFrame
