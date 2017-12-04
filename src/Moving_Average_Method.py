import pandas as pd
import numpy as np
import math


class MovingAverageMethod:
    def __init__(self, path, n):
        self.period = None
        self.prediction_array = []
        self.error_array = []
        self.mean_error = None
        self.n = n
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
        cumulative = 0
        for x in range(self.n):
            self.prediction_array.append(0)
            cumulative += self.df[x][0]
        print("Calculating prediction values...")
        for item in range(self.n, self.period):
            self.prediction_array.append(int(cumulative/self.n))
            cumulative = (cumulative+self.df[item][0])-self.df[item - self.n][0]
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
        self.mean_error = np.sum(self.error_array)/(self.period - self.n)
        return self.mean_error


ls = MovingAverageMethod(path="sales.csv", n=4)
print(ls.calculate_predicts())
print(ls.calculate_errors())
print(ls.error_array)
