# Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv',index_col="Month")

# Drop all NAN values
airline.dropna(inplace=True)
# Establishing the index to be the dates..
airline.index = pd.to_datetime(airline.index)

# Creating an exponential simple moving average
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(airline['Thousands of Passengers'], model='multiplicative')
result.plot()
plt.legend()

plt.show()
