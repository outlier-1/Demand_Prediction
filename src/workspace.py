from src.utils import plot_sales
from src.Average_Based_Methods.LastPeriod import LastPeriod
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a = LastPeriod(path='sales.csv', estimate_method='MAE')
a.calculate_predictions()
a.estimate_predictions()
sales = a.prediction_array[1:]
dates = a.dates.values[1:]
x = pd.Series(sales, index=dates)
x.plot()

plt.show(block=True)


