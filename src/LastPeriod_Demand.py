import pandas as pd
import numpy as np
import math


class LastPeriodPrediction:
    def __init__(self, path):
        self.period = None
        self.prediction_array = []
        self.error_array = []
        self.mean_error = None
        self.df = self.read_csv_file(data_path=path)

    def read_csv_file(self, data_path):
        try:
            self.df = pd.read_csv(data_path, sep=';', encoding='latin1', parse_dates=['Donem'], dayfirst=True,
                                  index_col='Donem')
            self.df = np.asarray(self.df, dtype='int')
            self.period = len(self.df)
            return self.df
        except FileNotFoundError:
            print("File couldn't found.")

    def calculate_predicts(self):
        self.prediction_array.append(0)
        print("Calculating prediction values...")
        for item in range(1, self.period):
            self.prediction_array.append(self.df[item-1][0])
        print("Done!")
        return self.prediction_array

    def calculate_errors(self):
        # Calculate the error array first
        self.error_array.append(0)
        print("Calculating Errors..!")
        for item in range(1, self.period):
            self.error_array.append(int(math.fabs(self.prediction_array[item] - self.df[item][0])))
        print("Done!")
        # Then calculate the mean error and return that.
        self.mean_error = np.sum(self.error_array)/(self.period - 1)
        return self.mean_error
