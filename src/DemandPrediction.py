import pandas as pd
import numpy as np
import math


# Gonna use that class for parent class.
class DemandPrediction:
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
