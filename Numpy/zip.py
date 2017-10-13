# 可以互换指定区域的位置
l = [1,2,3,4,5,6]
print(l[3:6] + l[0:3])
# 成对获取x, y的值
a = [1,2,3]
b = [4,5,6]
for x, y in zip(a, b):
  print(x, y)
