import numpy as np
a = np.array([1, 2, 3])
print(type(a))
# 维数
print(a.shape)
a[0] = 4
print(a)

b = np.array([[1,2,3], [4,5,6]])
print(b)
# 矩阵维数
print(b.shape)
print(b[1][2], b[0][0])
