import numpy
from pandas import DataFrame, Series
d = {
  'one': Series([1,2,3], index=['a','b','c']),
  'two': Series([1,2,3,4], index=['a','b','c','d'])
}

df = DataFrame(d)
print(df)
print(df.apply(numpy.mean))
# two 项
print(df['two'].map(lambda x:x > 1))
# 全应用
print(df.applymap(lambda x:x > 3))
