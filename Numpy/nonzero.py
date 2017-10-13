# 函数返回矩阵中非0元素的位置
from numpy import nonzero
x =[[1,0,0,0,2], [0,0,3,0,0]]
print(nonzero(x)[0])
'''
第一行是所有非零数所在行值
第二行是所有非零值所在列值
'''
