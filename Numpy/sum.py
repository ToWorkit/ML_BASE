# 求和
from numpy import sum
x = [[0,1,2], [2,1,0]]
b = [1,3,5,6]
print(sum(b))
print(sum(x))
# 列
print(sum(x, 0))
# 行
print(sum(x, 1))
