# 将矩阵进行转置
# T
from numpy import transpose, mat
a = [[1], [2], [3]]
print(type(a))
a = mat(a)
print(type(a))
print(a)
print(a.transpose())
print(a.T)
