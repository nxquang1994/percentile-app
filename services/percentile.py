import math

class Percentile():
    def __init__(self, percentile, values):
        if percentile > 1:
            self.percentile = percentile / 100
        else:
            self.percentile = percentile
        self.values = values
    
    def get_quantile(self): pass
    def get_pos(self): pass
    def get_total_count(self): pass
    def get_value(self): pass

    def get_indexes(self): 
        pos = self.get_pos()
        value = self.get_value()
        total_count = self.get_total_count()
        dict_res = {
            'value': value,
            'total_count': total_count
        }
        return dict_res


