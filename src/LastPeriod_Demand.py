from src.DemandPrediction import DemandPrediction


class LastPeriod(DemandPrediction):
    def __init__(self, path, estimate_method):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)

    def calculate_predictions(self):
        print("Calculating prediction values...")
        self.prediction_array[0] = None
        for item in range(1, self.period):
            self.prediction_array[item] = self.df[item - 1][0]
        print("Done!")
        return self.prediction_array


s = LastPeriod(path='sales.csv', estimate_method='OPT')
