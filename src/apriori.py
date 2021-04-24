
import pandas as pd
import numpy as np
import os


class Arules:
    def __init__(self):
        print('hi there')

    def read(self):
        dir = os.getcwd()
        data = pd.read_csv(dir + '/src/Project1 - groceries.csv')
        print(data)

    def get_frequent_item_sets(self, transactions=None, min_support=None, min_confidence=None):
        pass

    def get_arules(self, min_support=None, min_confidence=None, min_lift=None, sort_by='lift'):
        pass
    # sort_by: lift , confidence, support
