# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
从本地proxy文件中读取代理列表然后随机选择供spider使用
'''
from xiubai.middlewares.proxy import proxies
import random

class RandomProxy(object):
    def process_request(self, request, spider):
        # 随机代理
        proxy = random.choice(proxies)

        request.meta['proxy'] = 'http://%s' % proxy