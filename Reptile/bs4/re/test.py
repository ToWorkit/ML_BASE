# -*- coding: utf-8 -*-
import re

test = 'Hello World my name is Hlc'

l = re.findall('l+', test)

print(l)

str = 'hello, world, life is short, use Python'

a = re.search(r'\w+', str)
print(a.group())

# 控制标记
b = re.search(r'w.+D', str, re.I)
print(b.group())

# 查找所有
all = re.findall(r'\w+', str)
print(all)

# 先把正则进行编译，在进行查找，就能大量节省时间，增加效率
str_1 = 'hello World'
re1 = re.compile(r'h.{3}o')
print(re1.findall(str_1))