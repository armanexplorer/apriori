from pandas.core.frame import DataFrame
from apriori import Arules
import pandas as pd


df:DataFrame = pd.read_csv('Project1 - groceries.csv', header = None, squeeze = True, keep_default_na=False)
a = Arules()
d = a.get_frequent_item_sets(df.values, min_support=0.005, min_confidence=0.2)
print(d)
print(len(d))


# df:DataFrame = pd.read_csv('Project1 - groceries.csv', header=None, keep_default_na=False)
# r = df.shape[0]
# print(df.values)
# all = df.to_records(col)
# print(all[0])
# print(df[:][:1])
# print(df.unique())
# k1 = []
# for i in range(1,10):
#     print(df[:][[i]])
    # print(df[:][:1])
    # k1 += list(df[col].unique())
# print(len(k1))
# print(df.count())
# for a in df.head():
#     print(a)
# print(df.head())
# print(df)