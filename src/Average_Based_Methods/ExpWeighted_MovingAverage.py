from src.DemandPrediction import DemandPrediction


class ExpWeightedMovAverage(DemandPrediction):
    def __init__(self, path, estimate_method, alpha):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)
        self.alpha = alpha

    def calculate_predicts(self):
        self.prediction_array[0] = self.sales.values[0]
        print("Calculating prediction values...")
        for item in range(1, self.period_length):
            value = (self.sales.values[item - 1] * self.alpha) + (self.prediction_array[item - 1] * (1 - self.alpha))
            self.prediction_array[item] = int(value)

        # Change first item to correct calculation of estimate
        self.prediction_array[0] = None

        print("Done!")
        return self.prediction_array


ls = ExpWeightedMovAverage(path='../sales.csv', estimate_method='MAE', alpha=0.7)
print(ls.calculate_predicts())
print(ls.estimate_predictions())
