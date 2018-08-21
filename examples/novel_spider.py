#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/21 14:43
"""

from functools import wraps
from urllib.parse import urlencode
from pyquery import PyQuery
import requests

#定义一个装饰器来处理异常
def error(func):
    @wraps(func)
    def error_handler(kw):
        try:
            data=func(kw)
            return data
        except requests.exceptions.RequestException as e:
            print(e.args)
            str=input('A-再试一次\nB-退出：')
            if str=='A':
                error_handler(kw)
            elif str=='B':
                return False
    return error_handler


# 传入小说名字，返回搜获结果
@error
def get_novel(novel_name):
    novel_list = []
    base_url = 'https://www.owllook.net/search?'
    url = base_url + urlencode({'wd': novel_name})
    # items=PyQuery(url) 这样也可以
    response = requests.get(url, timeout=2)
    if response.status_code == 200:
        doc = PyQuery(response.text)
        items = doc('.result_item.col-sm-9.col-xs-12').items()
        for item in items:
            if item('.label.label-primary.parse-label'):
                novel = {}
                novel['novel_name'] = item('li').children('a').text()
                novel['url'] = item('li').children('a').attr('href')
                novel['origin_url'] = item('.netloc a').attr('href')
                novel_list.append(novel)
        return novel_list


# 打印搜索结果，
def print_novel_list(novel_list):
    if novel_list:
        num = 0
        print('查询结果如下：')
        for i in novel_list:
            str = '{}----{}'.format(num, i['novel_name'])
            print(str)
            num += 1
        return True


# 解析小说页面，返回各章节信息 传入一个小说信息字典
@error
def get_zhangjie(item):
    zhangjie_list = []
    base_url = 'https://www.owllook.net'
    novel_url = base_url + item['url']
    response = requests.get(novel_url, timeout=5)
    if response.status_code == 200:
        lis = PyQuery(response.text)('.mulu_list li').items()
        for li in lis:
            zhangjie_1 = (li('a').text(), li('a').attr('href'))
            # 构造单个章节的完整链接
            chapter_url = make_zhangjie_url(item, zhangjie_1)
            chapter = (zhangjie_1[0], chapter_url)
            # 打印章节的标题
            print(chapter[0])
            zhangjie_list.append(chapter)
        return zhangjie_list


# 构造单个章节的链接
def make_zhangjie_url(item, zhangjie):
    # https://www.owllook.net/owllook_content?
    # url=https://www.ybdu.com/xiaoshuo/2/2469/240070.html
    # &name=校园贵公子%第一章%格斗天王
    # &chapter_url==https://www.ybdu.com/xiaoshuo/2/2469/&novels_name=黑道公子
    base_url = 'https://www.owllook.net/owllook_content?'
    oringin_url = str('url=') + str(item['origin_url'])+ str(zhangjie[1])
    name = '&name=' + '%'.join(zhangjie[0].split())
    novel_url = '&chapter_url=' + item['url'].strip('/chapter?url')
    zhangjie_url = base_url + oringin_url + name + novel_url
    return zhangjie_url


#打印单个章节的内容
@error
def print_chapter_content(zhangjie_list):
    num=int(input('输入章节：'))
    res=requests.get(zhangjie_list[num+1][1],timeout=5)
    if res.status_code==200:
        doc=PyQuery(res.text)
        title=doc('#content_name').text()
        print(title)
        content=doc('#htmlContent').text()
        print(content)
        print(title)


def main():
    if True:
            novel_name = input('输入小说名:')
            novel_list = get_novel(novel_name)
            if print_novel_list(novel_list):
                novel_num = int(input('\n输入查看的小说序号：'))
                zhangjie_list = get_zhangjie(novel_list[novel_num])
                while zhangjie_list:
                    print_chapter_content(zhangjie_list)



if __name__ == '__main__':
    main()






