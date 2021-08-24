import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

def adfCheck(timeSeries):

    result = adfuller(timeSeries)
    print("Augmented Dicky-Fuller Test")

    labels = ["ADF Test Statistic", "P-value", "# of lags", "Num of Observations Used"]

    for value, label in zip(result, labels):
        print(label + ' : ' + str(value))

    if result[1] <= 0.05:
        print("""
        * Strong Evidence Against Null Hypothesis")
        * Reject Null Hypothesis
        * Data has no unit root, and is therefore stationary""")

    else:
        print("""
        * Weak evidence against null hypothesis
        * Failed to reject null hypothesis
        * Data has a unit root, and it's therefore non-stationary
        """)





# Arima Code Along
dataFrame = pd.read_csv('monthly-milk-production-pounds-p.csv')
dataFrame.columns = ["Month" , "Milk in Pounds per Cow"]


# Dropping the tail of the pandas dataframe
dataFrame.drop(168, axis=0, inplace=True)

dataFrame["Month"] = pd.to_datetime(dataFrame["Month"])
dataFrame.set_index("Month", inplace=True)

timeSeries = dataFrame["Milk in Pounds per Cow"]



# Calculating the Augmented Dickie Fuler
adfCheck(dataFrame["Milk in Pounds per Cow"])

dataFrame["First Difference"] = dataFrame["Milk in Pounds per Cow"] - dataFrame["Milk in Pounds per Cow"].shift(1)
dataFrame["First Difference"].plot()
adfCheck(dataFrame["First Difference"].dropna())
plt.show()

# If the first difference doesn't provide the evidence it's stationary, lets find
# The second difference, if even in the second difference the data is not stationary,
# Then the data is truly non-stationary
dataFrame["Milk Second Difference"] = dataFrame["First Difference"] - dataFrame["First Difference"].shift(1)
adf_Check = (dataFrame["Milk Second Difference"].dropna())

dataFrame["Milk Second Difference"].plot()
plt.show()


dataFrame["Seasonal First Difference"] = dataFrame["First Difference"] - dataFrame["First Difference"].shift(12)
dataFrame["Seasonal First Difference"].plot()

adfCheck(dataFrame["Seasonal First Difference"].dropna())


#                                      ACF and PACF

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

acf_plot = plot_acf(dataFrame["First Difference"].dropna())

plt.show()

seasonal_first = plot_acf(dataFrame["Seasonal First Difference"].dropna())
plt.show()

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(dataFrame["Seasonal First Difference"].dropna())
plt.show()

plot_pacf(dataFrame["Seasonal First Difference"].dropna())


# Forecasting future data points using ARIMA..
from statsmodels.tsa.arima_model import ARIMA

# Using the SARMIAX model to make future projections..
model = sm.tsa.statespace.SARIMAX(dataFrame["Milk in Pounds per Cow"], order=(0,1,0) , seasonal_order=(1,1,1,12))
results = model.fit()
print(results.summary())


# Plotting our SARMIAX data
plt.show()
results.resid.plot(kind="kde")
plt.show()


# Making forecast
dataFrame["forecast"] = results.predict(start=150, end=168)
dataFrame[["Milk in Pounds per Cow","forecast"]].plot()
plt.show()

# to make forecast in the future, we need more time periods.
from pandas.tseries.offsets import DateOffset

# Creates future dates..
futureDates = [dataFrame.index[-1] + DateOffset(months=x) for x in range(1,24)]
futureDataFrame = pd.DataFrame(index=futureDates, columns=dataFrame.columns)
final_dataFrame = pd.concat([dataFrame, futureDataFrame])

final_dataFrame["forecast"] = results.predict(start=168, end=202)
final_dataFrame[["Milk in Pounds per Cow","forecast"]].plot()
plt.show()
