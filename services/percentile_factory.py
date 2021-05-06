from services.percentile import Percentile
from services.normal_percentile import NormalPercentile

class PercentileFactory:
    @staticmethod
    def create_strategy(percentile, values, strategy):
        if strategy == 'basic':
            return NormalPercentile(percentile, values)
        return None