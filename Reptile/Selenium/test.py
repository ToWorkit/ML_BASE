'''
selenium模拟浏览器爬虫
代理url：http://www.kuaidaili.com/
'''
from selenium import webdriver
class Item(object):
    '''
        item类 表示每一个爬到的代理
        模拟Scrapy框架
        需要的代理当中的数据
    '''
    # ip地址
    ip = None
    # 端口
    port = None 
    # http 还是 https
    type = None
    # 物理地址
    local = None
    # 速度
    speed = None
    
class GetProxy(object):
    '''
        获取代理的类
    '''
    def __init__(self):
        '''
            初始化整个类
        '''
        self.starturl = 'http://www.kuaidaili.com/free/inha/'
        # urls列表
        self.urls = self.get_urls()
        # 爬取的代理列表
        self.proxy_list = self.get_proxy_list(self.urls)
        # 文件名
        self.filename = 'proxy.txt'
        # 保存
        self.saveFile(self.filename, self.proxy_list)
        
    def get_urls(self):
        '''
            返回一个代理url的列表
        '''
        urls = []
        # 来两页
        for i in range(1, 3):
            print(i)
            url = self.starturl + str(i)
            urls.append(url)
        return urls
    def get_proxy_list(self, urls):
        '''
            返回抓取到代理的列表
            整个爬虫的关键位置
        '''
        # 建立对象
        browser = webdriver.PhantomJS()
        proxy_list = []
        
        for url in urls:
            browser.get(url)
            browser.implicitly_wait(3)
            # 找出网页代理地址table的位置
            elements = browser.find_elements_by_xpath('//tbody/tr')
            for element in elements:
                # Item对象
                item = Item()
                item.ip = element.find_element_by_xpath('./td[1]').text
                item.port = element.find_element_by_xpath('./td[2]').text
                item.anonymous = element.find_element_by_xpath('./td[3]').text
                item.local = element.find_element_by_xpath('./td[4]').text
                item.speed = element.find_element_by_xpath('./td[5]').text
                proxy_list.append(item)
        # 退出
        browser.quit()
        return proxy_list
    def saveFile(self, filename, proxy_list):
        '''
            将爬取到的结果写入本地
        '''
        with open(filename, 'w') as f:
            for item in proxy_list:
                f.write(item.ip + '\t')
                f.write(item.port + '\t')
                f.write(item.anonymous + '\t')
                f.write(item.local + '\t')
                f.write(item.speed + '\t\n')
if __name__ == '__main__':
    Get = GetProxy()
