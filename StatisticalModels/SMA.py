# Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv('airline_passengers.csv',index_col="Month")

# Drop all NAN values
airline.dropna(inplace=True)
# Establishing the index to be the dates..
airline.index = pd.to_datetime(airline.index)


# Creating two simple moving averages of 6 and 12 day intervals.
airline['6-month-SMA']=airline['Thousands of Passengers'].rolling(window=6).mean()
airline['12-month-SMA']=airline['Thousands of Passengers'].rolling(window=12).mean()

print(airline)

airline['6-month-SMA'].plot(color="blue")
airline['12-month-SMA'].plot(color="green")
airline['Thousands of Passengers'].plot(color="red")
plt.legend()

plt.show()
