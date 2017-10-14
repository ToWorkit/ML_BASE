# !/usr/bin/python
# -*- coding: utf-8 -*-

# 通过User-Agent来控制访问
# 可以自己设置一下user-agent，或者更好的是，我们从一系列的user-agent里随机挑出一个符合标准的使用
def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = agents[random.randint(0, len(agents))]
    return fakeheader

    # 注意看新的请求函数：

def get_html(url):
    try:
        r = requests.get(url, timeout=30,headers=get_agent())
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.status_code
    except:
        return "Someting Wrong！"


# 通过IP限制来反爬虫
# 比较成熟的方式是：IP代理池 简单的说，就是通过ip代理，从不同的ip进行访问，这样就不会被封掉ip了。 可是ip代理的获取本身就是一个很麻烦的事情，网上有免费和付费的，但是质量都层次不齐。如果是企业里需要的话，可以通过自己购买集群云服务来自建代理池

def get_proxy():
    '''
    简答模拟代理池
    返回一个字典类型的键值对，
    '''
    proxy = ["http://116.211.143.11:80",
             "http://183.1.86.235:8118",
             "http://183.32.88.244:808",
             "http://121.40.42.35:9999",
             "http://222.94.148.210:808"]
    fakepxs = {}
    fakepxs['http'] = proxy[random.randint(0, len(proxy))]

    return fakepxs

# 通过JS脚本来防止爬虫
# PhantomJS是一个Python包，他可以在没有图形界面的情况下，完全模拟一个”浏览器“，对你没看错，就是浏览器，这样的话，js脚本验证什么的再也不是问题了




# 通过robots.txt来限制爬虫
# robots.txt（统一小写）是一种存放于网站根目录下的ASCII编码的文本文件，它通常告诉网络搜索引擎的漫游器（又称网络蜘蛛），此网站中的哪些内容是不应被搜索引擎的漫游器获取的，哪些是可以被漫游器获取的。因为一些系统中的URL是大小写敏感的，所以robots.txt的文件名应统一为小写。robots.txt应放置于网站的根目录下。如果想单独定义搜索引擎的漫游器访问子目录时的行为，那么可以将自定的设置合并到根目录下的robots.txt，或者使用robots元数据（Metadata，又称元数据）。 robots.txt协议并不是一个规范，而只是约定俗成的，所以并不能保证网站的隐私。注意robots.txt是用字符串比较来确定是否获取URL，所以目录末尾有与没有斜杠“/”表示的是不同的URL。robots.txt允许使用类似"Disallow: *.gif"这样的通配符[1][2]