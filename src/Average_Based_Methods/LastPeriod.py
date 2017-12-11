from src.DemandPrediction import DemandPrediction
from src.utils import plot_sales
import numpy as np


class LastPeriod(DemandPrediction):
    def __init__(self, path, estimate_method):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)

    def calculate_predictions(self):
        print("Calculating prediction values...")
        self.prediction_array[0] = np.nan
        for item in range(1, self.period_length):
            self.prediction_array[item] = self.sales.values[item - 1]
        print("Done!")
        return self.prediction_array


# s = LastPeriod(path='../sales.csv', estimate_method='MAE')
# s.calculate_predictions()
# print(s.prediction_array)
# print(s.estimate_predictions())

