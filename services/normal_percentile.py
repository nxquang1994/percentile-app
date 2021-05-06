import math
from services.percentile import Percentile


class NormalPercentile(Percentile):
    def __init__(self, percentile, values):
        super().__init__(percentile, values)

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
        pos = self.percentile * (len(self.values) + 1)
        return math.floor(pos)

    
    def get_total_count(self):
        return len(self.values)


    def get_indexes(self):
        len_values = len(self.values)
        sorted_values = sorted(self.values)
        if quantile == False:
            return 'Percentile is invalid'
        pos = self.get_pos()
        value = self.values[pos - 1]
        total_count = self.get_total_count()
        dict_res = {
            'value': value,
            'total_count': total_count
        }
        return dict_res