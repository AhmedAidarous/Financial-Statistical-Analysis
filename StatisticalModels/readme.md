# EWMA And The Simlpe Moving Average
In a nutshell, the Simple Moving Average **(SMA)** is a technical indicator which is used to visualize trends on a 
and n-number of sampling periods, in securities more specifically it A simple moving average (SMA) calculates the 
average of a selected range of prices, usually closing prices, by the number of periods in that range. 

A benefit to using such an indicator is it can aid in determining if an asset price will continue or if it will 
reverse a bull or bear trend.

# Simple Moving Average Formula
The formula to calculate the Simple Moving Average (SMA) is the following:
<br>
![image](https://user-images.githubusercontent.com/47617364/130436725-09e634df-d07b-4a23-8ead-ef4cf110b96a.png)
<br>
Now here's an example of using an SMA:
![image](https://user-images.githubusercontent.com/47617364/130437313-7f75fbcd-98dc-4633-9128-016877f402d4.png)

As you can see, both 6-month and 12-month moving averages show thet trend of the data used in the example which was airline passengers throughout the 1940s - 1950s.

# Exponential Weighted Moving Average
Although SMA is a good indicator of trend, however it has some **"weaknesses"**:
<br>• Smaller more refined data will lead to more noise, rather than signal
<br>• The trend would never reach to full peak or valley of the data due to the averaging process
<br>• Doesn't really inform you about possible future behaviour, all it really does is describe trends in data
<br>• Extreme anomalies in historical data can skew the SMA significantly

Therefore to avoid these issues, we can use an EWMA (Exponentially Weighted Moving Average), EWMA will allow us to reduce the sort of lag effect from using SMA, and it will put more weight on values that occured more recently. The weighting process will depend on the actual parameters used in the EWMA and the number of periods given a window size. 

The formula to calculate this trend indicator is the following:
![image](https://user-images.githubusercontent.com/47617364/130439555-55cdc59c-e7ab-49bf-bb98-d91ee3c37d22.png)
<br>
Where:
<br>• w : Denotes the applied weight
<br>• x : The input value
<br>• y : The output average weighted result
and t is the iterative time-period,

Expanding this formula, you will get:
![image](https://user-images.githubusercontent.com/47617364/130439742-4652544b-9438-4427-9a16-f36d37b098e8.png)

The added parameter here is alpha (a), this is the smoothing factor.

The following is an example of using EWMA:
![image](https://user-images.githubusercontent.com/47617364/130440195-091f72fb-ba07-49b8-988e-f7aebc08f7cd.png)

As you can see, the EWMA accounts for peaks of the trend.

# ETS Decomposition
We can use an additive model when it seems that the trend is more linear, as well as the seasonality and trend components seem to be constant over time, for example, every year there are almost 1000 new passengers. A multiplicative model is more appropriate when we are increasing or decreasing a non-linear rate, so for example, each year the airline exponentially doubles the amount of passengers, and that is something ETS can measure. 

## Using ETS
To use ETS you need to import the following following module

    pip install statsmodels

If we run the ETS model on the same dataset used above which was airline data, it would look like the following:
![image](https://user-images.githubusercontent.com/47617364/130442247-f69cbc6e-47f6-46aa-819b-6a836fe8efd0.png)

So as you can see, the following are some of the characteristics calculated by the ETS decomposition:
<br>• **Trend**
<br>• **Seasonal**
<br>• **Residual**

# Autoregressive Integrated Moving Average (ARIMA)
An autoregressive integrated moving average, or ARIMA, is a statistical analysis model that uses time series data to either better understand the data set or to predict future trends. 

A statistical model is autoregressive if it predicts future values based on past values. For example, an ARIMA model might seek to predict a stock's future prices based on its past performance or forecast a company's earnings based on past periods. However these models don't work well with historical stock data.



Now there are two types of ARIMA models, these are:
<br>• **Non-Seasonal ARIMA**
<br>• **Seasonal ARIMA**

## Non-Seasonal ARIMA
These models are used on non-seasonal data, and they are denoted as ARIMA (p,d,q) where p,d, and q are non-negative integers. The following describes the three denotes:

**p** : A regression model that utilizes the dependent relationship between a current observation and observations over a previous period. 

**d** : Differencing on observations such as Subtracting an observation from an observation at the previous time step. In order to make the time series stationary.  

**q** : A model that uses the dependency between an observation and a residual error from a moving average model applied to lagged observations. 


### Stationary vs Non-Stationary Data
To effectiely use ARIMA, we need to understand stationarity in our data. What makes a data set stationary is a stationary series has constant **mean and variance over time**. Therefore a stationary dataset will allow our model to predict that the mean and the variance will be the same in future periods. Now the following a few examples of stationary data:
There are three 
<br>

![image](https://user-images.githubusercontent.com/47617364/130454799-384a9386-0521-4f91-a6d8-4d0bb91ae58d.png)

![image](https://user-images.githubusercontent.com/47617364/130454985-cb41bec9-2d43-40ae-b0db-ab56fc4f72f8.png)

![image](https://user-images.githubusercontent.com/47617364/130456056-047904e2-0980-451c-bf72-04d78b695ce8.png)
<br> Visually the wavelengths must be constant

A common way to mathematically test the data, and see if it's stationary is through the use of the **Augmented Dicky-Fuller test**

Now if you've determined that your data is not stationary, you will need to transform ir to be stationary in order to evaluate it and what type of ARIMA terms you will use. 

One simple way to do this is through *differencing*, the following explains the intuition behind the concept:

### Differencing
![image](https://user-images.githubusercontent.com/47617364/130456740-5cf943ee-1a58-4ab0-bac5-cdcf22229e14.png)

This is the concept of subtracting element with element - 1. You can continue differencing until you reach stationarity, however each differencing step comes at the cost of losing a row of data.





