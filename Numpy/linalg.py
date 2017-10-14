# 逆矩阵
from numpy import diag, linalg, mat
d = [1,2,3]
dd = diag(d)
print(dd)
print(linalg.inv(dd))
print(mat(dd).I)

l = [[1,2,3], [4,5,6], [7,8,9]]
print(mat(l))
