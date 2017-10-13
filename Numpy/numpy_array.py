import numpy as np
# 维数
a = np.random.random((3, 4))
print(a)

# 取到2，从1开始取到3，含头不含尾
b = a[:2, 1:3]
print(b)

row_r1 = a[1, :]
row_r2 = a[1:2, :]
# 区别
# 使用切片语法访问数组时，得到的是原数组的子集
print(row_r1)
print(row_r2)
print('------------------------------')

ar = np.random.random((4, 2))
print(ar)
# 行(row) 列(col)
print(ar[[0,1,2], [0,1,0]])
print(ar[[0,0], [1,1]])
print('----------------------------------')

x = np.array([1,2])
# int32
print(x.dtype)
x = np.array([1.1,2.3])
# float64
print(x.dtype)
x = np.array([1,2], dtype=np.int64)
# int64
print(x.dtype)
