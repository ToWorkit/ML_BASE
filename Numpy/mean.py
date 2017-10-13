# 均值
from numpy import mean
b = [1,3,5,6]
print(mean(b))
l = [[1,2,3,4,5,6],[3,4,5,6,7,8]]
# 全部元素求均值
print(mean(l))
# 按列求均值
print(mean(l, 0))
# 按行求均值
print(mean(l, 1))
