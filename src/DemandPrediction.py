import pandas as pd
import numpy as np


# Gonna use that class for parent class.
class DemandPrediction:
    Estimate_Methods = ['MAE', 'MSE', 'MAPE', 'SMAPE', 'OPT']

    def __init__(self, path, estimate_method):
        assert estimate_method in DemandPrediction.Estimate_Methods, 'Estimate method is not valid.' \
                                                                     ' Please choose a valid method.'
        self.estimate_method = estimate_method
        self.df, self.period = DemandPrediction.read_csv_file(data_path=path)
        self.prediction_array = np.zeros(shape=self.df.shape)
        self.error_array = np.zeros(shape=self.df.shape)
        self.mean_error = None

    def estimate_predictions(self):
        if self.estimate_method is 'MAE':
            return DemandPrediction.calc_mean_absolute_error(df=self.df, prediction_array=self.prediction_array)

        elif self.estimate_method is 'MSE':
            return DemandPrediction.calc_mean_squared_error(df=self.df, prediction_array=self.prediction_array)

        elif self.estimate_method is 'MAPE':
            return DemandPrediction.calc_mean_absolute_percentage_error(df=self.df,
                                                                        prediction_array=self.prediction_array)

        elif self.estimate_method is 'SMAPE':
            return DemandPrediction.calc_sym_mean_absolute_percentage_error(df=self.df,
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
            df = pd.read_csv(data_path, sep=';', encoding='latin1', parse_dates=['Period'], dayfirst=True,
                                  index_col='Period')
            df = np.asarray(df, dtype='int')
            period = len(df)
            return df, period
        except FileNotFoundError:
            print("File couldn't found.")

    @staticmethod
    def calc_mean_squared_error(df, prediction_array):
        assert df.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
                break
        error_array = np.power(np.subtract(df, prediction_array), 2)
        mean_squared_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_squared_error, error_array

    @staticmethod
    def calc_mean_absolute_error(df, prediction_array):
        assert df.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
        error_array = np.absolute(np.subtract(df, prediction_array))
        mean_absolute_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_absolute_error, error_array

    @staticmethod
    def calc_mean_absolute_percentage_error(df, prediction_array):
        assert df.shape == prediction_array.shape, "Inconsistent Shape Error.\n" \
                                             "Prediction array must have the same shape with DataFrame"
        error_number = None
        _index = 0
        for item in prediction_array:
            _index += 1
            if np.isnan(item):
                error_number = _index
                break
        error_array = np.divide(np.absolute((np.subtract(df, prediction_array))), df)
        mean_absolute_percentage_error = np.nansum(error_array) / (len(prediction_array) - error_number)
        return mean_absolute_percentage_error, error_array

    @staticmethod
    def calc_sym_mean_absolute_percentage_error(df, prediction_array):
        pass

    @staticmethod
    def find_optimum_method():
        pass


