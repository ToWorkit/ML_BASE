# 协方差
from numpy import cov, sum, multiply, mean
b = [1,3,5,6]
print(cov(b))
# 推
print(sum((multiply(b,b))-mean(b)*mean(b))/3)

# cov的参数是矩阵
# 输出结果也是矩阵
# 输出的矩阵为协方差矩阵
x = [[0, 1, 2],[2, 1, 0]]
print(cov(x))
print(sum((multiply(x[0],x[1]))-mean(x[0])*mean(x[1]))/2)
