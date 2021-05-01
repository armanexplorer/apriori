
import pandas as pd
import numpy as np
import os


class Arules:
    def __init__(self):
        pass

    def get_frequent_item_sets(self, transactions=None, min_support=None, min_confidence=None):
        d = dict()
        num = len(transactions)
        for r in transactions:
            for w in r:
                if w == '':
                    break
                d[w] = d.get(w, 0) + 1
        w = num * min_support
        for k, v in d.copy().items():
            if(v<w):
                del d[k]
        return d

    def get_arules(self, min_support=None, min_confidence=None, min_lift=None, sort_by='lift'):
        pass
    # sort_by: lift , confidence, support
