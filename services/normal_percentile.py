import math
from services.percentile import Percentile


class NormalPercentile(Percentile):
    def __init__(self, percentile, values):
        super().__init__(percentile, values)
        self.sorted_values = sorted(values)

    def get_quantile(self):
        if self.percentile < 25:
            return 1
        if self.percentile < 50:
            return 2
        if self.percentile < 75:
            return 3
        if self.percentile < 100:
            return 4
        return False

    def get_pos(self):
        pos = math.ceil(self.percentile * len(self.values))
        return pos

    def get_value(self):
        pos = self.get_pos()
        return self.sorted_values[pos - 1]

    
    def get_total_count(self):
        return len(self.values)


