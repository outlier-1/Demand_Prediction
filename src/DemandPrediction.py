import pandas as pd
import numpy as np


# Gonna use that class for parent class.
class DemandPrediction:
    Estimate_Methods = ['MAE', 'MSE', 'MAPE', 'SMAPE', 'OPT']

    def __init__(self, path, estimate_method):
        assert estimate_method in DemandPrediction.Estimate_Methods, 'Estimate method is not valid.' \
                                                                     ' Please choose a valid method.'
        self.estimate_method = estimate_method
        self.df, self.dates, self.sales, self.period_length = DemandPrediction.read_csv_file(data_path=path)
        self.prediction_array = np.zeros(shape=self.sales.values.shape)
        self.error_array = np.zeros(shape=self.sales.values.shape)
        self.mean_error = None

    def estimate_predictions(self):
        if self.estimate_method is 'MAE':
            return DemandPrediction.calc_mean_absolute_error(actual_sales=self.sales.values,
                                                             prediction_array=self.prediction_array)

        elif self.estimate_method is 'MSE':
            return DemandPrediction.calc_mean_squared_error(actual_sales=self.sales.values,
                                                            prediction_array=self.prediction_array)

        elif self.estimate_method is 'MAPE':
            return DemandPrediction.calc_mean_absolute_percentage_error(actual_sales=self.sales.values,
                                                                        prediction_array=self.prediction_array)

        elif self.estimate_method is 'SMAPE':
            return DemandPrediction.calc_sym_mean_absolute_percentage_error(actual_sales=self.sales.values,
                                                                            prediction_array=self.prediction_array)

        elif self.estimate_method is 'OPT':
            # It will find the optimum method for data set.
            pass
        else:
            raise ValueError

    def calculate_predictions(self):
        """ This method is going to be overridden by subclasses """
        pass

    @staticmethod
    def read_csv_file(data_path):
        try:
            # Read csv file
            df = pd.read_csv(data_path, sep=';', encoding='latin1')

            # Parse Data Frame into pandas.Series
            dates = df.iloc[:, 0]
            sales = df.iloc[:, 1]

            # Length Of Period
            period_length = len(df)

            return df, dates, sales, period_length
        except FileNotFoundError:
            print("File couldn't found.")

    @staticmethod
    def calc_mean_squared_error(actual_sales, prediction_array):
        assert actual_sales.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
                break
        error_array = np.power(np.subtract(actual_sales, prediction_array), 2)
        mean_squared_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_squared_error, error_array

    @staticmethod
    def calc_mean_absolute_error(actual_sales, prediction_array):
        assert actual_sales.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
        error_array = np.absolute(np.subtract(actual_sales, prediction_array))
        mean_absolute_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_absolute_error, error_array

    @staticmethod
    def calc_mean_absolute_percentage_error(actual_sales, prediction_array):
        assert actual_sales.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
                break
        error_array = np.divide(np.absolute((np.subtract(actual_sales, prediction_array))), actual_sales)
        mean_absolute_percentage_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_absolute_percentage_error, error_array

    @staticmethod
    def calc_sym_mean_absolute_percentage_error(actual_sales, prediction_array):
        pass

    @staticmethod
    def find_optimum_method():
        pass


