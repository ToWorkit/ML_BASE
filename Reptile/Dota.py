# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
初级爬虫进阶版，处理注释
'''
import requests, bs4

# 网页
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        # 请求成功
        r.raise_for_status()
        # 设置与源文件相同的coding
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'ERROR'

# 处理
def print_request(url):
    html = get_html(url)
    # 构建lxml
    soup = bs4.BeautifulSoup(html, 'lxml')
    # 找到所需内容的容器标签
    match_list = soup.find_all('div', attrs={'class': 'matchmain bisai_qukuai'})
    # 整体数据储存
    match_detail = []
    for match in match_list:
        # 储存每条数据字典
        detail = {}
        # 比赛时间(去掉首尾空格)
        detail['time'] = match.find('div', attrs={'class': 'whenm'}).text.strip()
        # 队名
        teamname =match.find_all('span', attrs={'class': 'team_name'})

        # 有时会因网站的构造原因造成队名不显示，需要过滤注释
        # 会显示一个php查询注释
        # <?php phpinfo(); ?>
        if teamname[0].string[0:3] == 'php':
            detail['team1_name'] = '暂无队名'
        else:
            detail['team1_name'] = teamname[0].string

        # 使用css选择器来查找数据
        # 队伍支持度
        detail['team1_suppoer_level'] = match.find('span', class_='team_number_green').string

        detail['team2_name'] = teamname[1].string
        detail['team2_support_level'] = match.find('span', class_='team_number_red').string
        # 将每一条数据都存入列表
        match_detail.append(detail)
    return match_detail

# 将内容写入到 Dota.txt 文件中
def writeFile(dict):
    print(dict)
    with open('Dota.txt', 'a+') as f:
        for item in dict:
            print(item)
            f.write('比赛时间: %s\n 参赛队伍: \n 队名: %s\t 支持度: %s\n 队名: %s\t 支持度: %s\n' % (item['time'], item['team1_name'], item['team1_suppoer_level'], item['team2_name'], item['team2_support_level']))
    print('数据写入完成')

def main():
    url = 'http://dota2bocai.com/match'
    dict_content =  print_request(url)
    writeFile(dict_content)

if __name__ == '__main__':
    main()