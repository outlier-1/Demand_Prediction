from src.DemandPrediction import DemandPrediction
import numpy as np


class WeightedMovingAverage(DemandPrediction):
    def __init__(self, path, estimate_method, weights):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)
        self.n = len(weights)
        self.weights = weights

    def calculate_predicts(self):
        for x in range(self.n):
            self.prediction_array[x] = None
        print("Calculating prediction values...")
        for item in range(self.n, self.period):
            cumulative = np.sum(np.multiply(self.weights, self.df[item - self.n: item]))
            self.prediction_array[item] = int(cumulative)
        print("Done!")
        return self.prediction_array


w = np.asarray([[0.1], [0.2], [0.3], [0.4]])
ls = WeightedMovingAverage(path="sales.csv", estimate_method='MAE', weights=w)
print(ls.calculate_predicts())
print(ls.estimate_predictions())
