from src.DemandPrediction import DemandPrediction


class SimpleAverageMethod(DemandPrediction):
    def __init__(self, path, estimate_method):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)

    def calculate_predicts(self):
        self.prediction_array[0] = None
        print("Calculating prediction values...")
        cumulative = 0
        for item in range(1, self.period):
            cumulative += self.df[item - 1][0]
            self.prediction_array[item] = int(cumulative/item)
        print("Done!")
        return self.prediction_array


ls = SimpleAverageMethod(path="sales.csv", estimate_method='MAE')
print(ls.calculate_predicts())
print(ls.estimate_predictions())
