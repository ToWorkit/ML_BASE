# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
requests bs4
3.6.3
ubuntn
初级爬虫，通过class 属性查找内容
'''
import requests
import time
from bs4 import BeautifulSoup

# 定义爬虫函数
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        # 成功
        r.raise_for_status()
        # 手动设置编码为utf-8
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'ERROR'

# print(get_html('http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'))

'''
分析贴吧的网页文件，整理信息，保存在列表变量中
'''
def get_content(url):
    # 初始化一个列表来保存所有的帖子信息
    comments = []
    # 将需要的网页信息保存到本地
    html = get_html(url)
    # 构建bs4
    soup = BeautifulSoup(html, 'lxml')
    # 找到所有指定类属性的li
    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})
    # 迭代
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 利用try...except防止爬虫找打不到信息而停止运行
        try:
            # 筛选出需要的信息，并保存到comment中
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit '}).text.strip()
            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': 'j_th_tit '})['href']
            comment['name'] = li.find(
                'span', attrs={'class': 'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('小蜘蛛要复活')
    return comments

'''
将爬取的文件写入本地
保存到当前目录的TTBT.text文件中
'''
def OutFile(dict):
    # 文件读取使用with
    # 附加读写
    with open('date.txt', 'a+') as f:
        for comment in dict:
            print(comment)
            # format 字符串格式化 %s
            f.write('标题: {}\t 链接：{}\t 发帖人：{}\t 发帖时间：{}\t 回复数量：{}\n'.format(comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))
    print('回来吧，小蜘蛛')

def main(base_url, deep):
    # 所有的url都保存
    url_list = []
    # 0 - deep
    for i in range(0, deep):
        # 页
        url_list.append(base_url + '&pn' + str(50*i))
    print('网页到手，开始处理数据')

    # 循环写入数据
    for url in url_list:
        # 拿数据
        content = get_content(url)
        # 处理数据
        OutFile(content)
    print('辛苦了小蜘蛛，数据以处理完毕')

base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
# 深度(页数)
deep = 6

# 作为脚本立即执行， import 导入无效
if __name__ == '__main__':
    main(base_url, deep)