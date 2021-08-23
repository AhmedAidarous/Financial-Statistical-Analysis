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
airline['EWMA12'] = airline['Thousands of Passengers'].ewm(span=12).mean()
airline['Thousands of Passengers'].plot(color="red")
airline['EWMA12'].plot(color="blue")
plt.legend()

plt.show()
