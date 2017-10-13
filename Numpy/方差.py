# std 标准方差
# var 方差
import numpy as np
from numpy import var, std, power
b = [1,3,5,6]
print(var(b))
print(std(b))

l = [[1,2,3,4,5,6], [3,4,5,6,7,8]]
print(var(l[0]))
print(var(l,0)) # 按列求方差
print(var(l,1)) # 按行求方差
