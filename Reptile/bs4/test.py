from bs4 import BeautifulSoup
# 构建
# 文件  指定解析器
soup = BeautifulSoup(open('one.html'), 'html.parser')
# print(soup.prettify())

# 找到文档的title
print(soup.title)
# title 的 name 值
print(soup.title.name)
# title 中的字符串String
print(soup.title.string)
# title 父节点的name属性
print(soup.title.parent.name)
# 文档中第一个找到的段落
print(soup.p)
# class 值
print(soup.p['class'])
# 找到所有的a标签
print(soup.find_all('a'))
for link in soup.find_all('a'):
  print(link)
# 找到id值为link3的标签
print(soup.find(id='link3'))

# 只获取内容，不要标签
print(soup.get_text())
