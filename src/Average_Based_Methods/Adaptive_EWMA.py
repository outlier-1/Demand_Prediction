from src.DemandPrediction import DemandPrediction


class AdaptiveEWMA(DemandPrediction):
    def __init__(self, path, estimate_method, alpha):
        DemandPrediction.__init__(self, path=path, estimate_method=estimate_method)
        self.alpha = alpha

    def calculate_predicts(self):
        pass


ls = AdaptiveEWMA(path='../sales.csv', estimate_method='MAE', alpha=0.7)
print(ls.calculate_predicts())
print(ls.estimate_predictions())
