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

A statistical model is autoregressive if it predicts future values based on past values. For example, an ARIMA model might seek to predict a stock's future prices based on its past performance or forecast a company's earnings based on past periods. 



