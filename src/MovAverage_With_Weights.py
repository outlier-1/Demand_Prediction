import pandas as pd
import numpy as np
import math


class WeightedMovingAverage:
    def __init__(self, path, weights):
        self.period = None
        self.prediction_array = []
        self.error_array = []
        self.mean_error = None
        self.n = len(weights)
        self.weights = weights
        self.df = self.read_csv_file(data_path=path)

    def read_csv_file(self, data_path):
        try:
            self.df = pd.read_csv(data_path, sep=';', encoding='latin1', parse_dates=['Period'], dayfirst=True,
                                  index_col='Period')
            self.df = np.asarray(self.df, dtype='int')
            self.period = len(self.df)
            return self.df
        except FileNotFoundError:
            print("File couldn't found.")

    def calculate_predicts(self):
        for x in range(self.n):
            self.prediction_array.append(0)
        print("Calculating prediction values...")
        for item in range(self.n, self.period):
            cumulative = np.sum(np.multiply(self.weights, self.df[item - self.n: item]))
            self.prediction_array.append(int(cumulative))
        print("Done!")
        return self.prediction_array

    def calculate_errors(self):
        # Calculate the error array first
        for x in range(self.n):
            self.error_array.append(0)
        print("Calculating Errors..!")
        for item in range(self.n, self.period):
            self.error_array.append(int(math.fabs(self.prediction_array[item] - self.df[item][0])))
        print("Done!")
        # Then calculate the mean error and return that.
        self.mean_error = np.sum(self.error_array) / (self.period - self.n)
        return self.mean_error


w = np.asarray([[0.1], [0.2], [0.3], [0.4]])
ls = WeightedMovingAverage(path="sales.csv", weights= w)
print(ls.calculate_predicts())
print(ls.calculate_errors())
print(ls.error_array)
