import requests
# 百度
# hd = {'User-agent': 'Lp'}
r = requests.get('https://www.baidu.com')
# 打印浏览
print(r.text)
# print(r)
