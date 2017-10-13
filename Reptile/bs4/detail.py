'''
Tag： 和html中的Tag基本没有区别，可以简单上手使用
NavigableString： 被包裹在tag内的字符串
BeautifulSoup： 表示一个文档的全部内容，大部分的时候可以吧他看做一个tag对象，支持遍历文档树和搜索文档树方法。
Comment：这是一个特殊的NavigableSting对象，在出现在html文档中时，会以特殊的格式输出，比如注释类型。
'''
import bs4
soup = bs4.BeautifulSoup(open('./one.html'), 'html.parser')
print(soup.head)
print(soup.title)
# 第一个
print(soup.body.b)
