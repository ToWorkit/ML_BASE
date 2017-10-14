# !/usr/bin/python
# -*- coding: utf-8 -*-
import bs4, requests

# 抓取网页
def get_html(url):
    try:
        r = requests.get(url)
        # 成功
        r.raise_for_status()
        # 手动设置编码
        r.encoding = ('utf-8')
        return r.text
    except:
        return 'ERROR'

# 获取排行榜小说及其链接
'''
爬取每一类型小说排行榜
按顺序写入文件
文件内容为 小说名字+小说链接
将内容保存到列表并返回一个url链接地址的列表
'''
def get_content(url):
    url_list = []
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')

    # 分类
    category_list = soup.find_all('div', class_='index_toplist mbottom')

    for cate in category_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a+') as f:
            f.write("\n小说类别: %s\n" % name)

        # 通过style属性来定位总排行榜
        general_list = cate.find(style="display: block;")
        # 找到全部小说名字
        book_list = general_list.find_all('li')
        # 迭代出每个小说的名字和链接
        for book in book_list:
            link = 'http://www.qu.la/' + book.a['href']
            title = book.a['title']
            # 将文章的url地址保存到一个列表变量中
            url_list.append(link)
            # 修改模式为 a，防止文件被清空
            with open('novel_list.csv', 'a') as f:
                f.write("小说名: %s\t 小说地址: %s\t" % (title, link))
    return url_list

# 获取单本小说的所有章节并创建小说文件
def get_txt_url(url):
    url_list = []
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
    list_a = soup.find_all('dd')
    txt_name = soup.find('h1').text
    with open('./books/%s.txt' % txt_name, 'a+') as f:
        f.write('标题: %s' % txt_name)
    for url in list_a:
        url_list.append('http://www.qu.la/' + url.a['href'])

    return url_list, txt_name

# 获取小说每个章节的文本并写入本地
def get_one_txt(url, txt_name):
    # 处理特殊标签
    html = get_html(url).replace('<br/>', '\n')
    soup = bs4.BeautifulSoup(html, 'lxml')
    try:
        txt = soup.find('div', id='content').text.replace('chaptererror();', '')
        title = soup.find('title').text
        with open('./books/%s.txt' % txt_name) as f:
            f.write(title + '\n\n')
            f.write(txt)
            print('当前小说： %s 当前 %s 章已经下载完毕' % (txt_name, title))
    except:
        print('ERROR_')

