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
    def get_indexes(self): pass
    def get_total_count(self): pass


