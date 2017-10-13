# 相关系数矩阵
from numpy import corrcoef, mean, std, multiply
vc = [1,2,39,0,8]
vb = [1,2,38,0,8]
print(mean(multiply((vc-mean(vc)), (vb-mean(vb)))) / (std(vb) * std(vc)))
# corrcoef 得到相关系数矩阵(向量的相似程度)
print(corrcoef(vc, vb))
