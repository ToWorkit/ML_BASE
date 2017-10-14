# !/usr/bin/python
# -*- coding: utf-8 -*-
from scrapy.selector import Selector
body = open('demo.xml', 'r').read()
# print(body)

# 采集第一个class内容
print(Selector(text=body).xpath('/html/body/class[1]').extract())
# 采集最后一个class内容
print(Selector(text=body).xpath('/html/body/class[last()]').extract())
# 采集最后一个class中的name属性文本
print(Selector(text=body).xpath('/html/body/class[last()]/name/text()').extract())