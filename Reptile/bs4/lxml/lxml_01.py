# -*- coding: utf-8 -*-
import bs4
soup = bs4.BeautifulSoup(open('../one.html'),'lxml')
# print(soup.prettify())

# 返回所有的a标签
a_tag = soup.find_all('a')

print(a_tag[0])
# 将其子节点以列表的方式输出
print(a_tag[0].contents)

title_tag = soup.head.contents[0]
print(title_tag.contents)
for child in title_tag.children:
	print(child)

# 孙节点
for child in title_tag.descendants:
	print(child)

# a_tag 下的所有文本内容
for string in soup.strings:
	print(repr(string))

# soup.find_all('a')