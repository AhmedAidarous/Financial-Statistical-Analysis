
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
