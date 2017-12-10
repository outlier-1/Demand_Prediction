from src.DemandPrediction import DemandPrediction


class MovingAverageMethod(DemandPrediction):
    def __init__(self, path, estimate_method, n):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)
        self.n = n

    def calculate_predicts(self):
        cumulative = 0
        for x in range(self.n):
            self.prediction_array[x] = None
            cumulative += self.df[x][0]
        print("Calculating prediction values...")
        for item in range(self.n, self.period):
            self.prediction_array[item] = int(cumulative/self.n)
            cumulative = (cumulative+self.df[item][0]) - (self.df[item - self.n][0])
        print("Done!")
        return self.prediction_array


ls = MovingAverageMethod(path="../sales.csv", estimate_method='MAE', n=4)
print(ls.calculate_predicts())
print(ls.estimate_predictions())
