#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/8 14:32
"""
# from requests.exceptions import RequestException
import requests
import re
import os
from progressbar import *  # 用于显示进度条


# from tqdm import tqdm
# import time

# global number  #定义全局变量
# number = 0


# 爬取一个页面电影的url的尾部
def get_onepage_url(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    pattern = re.compile('<li>.*?href="(.*?)".*?<h3>(.*?)</h3>.*?</li>', re.S)
    URL = re.findall(pattern, response.text)  # 返回的是元祖类型
    return URL


# 爬取一个章节的电影的URL的尾部
def get_pages_url():
    URLs = []

    # 爬取多个章节的电影URL的尾部
    # kind_page = [87, 96, 111, 110, 113, 114, 130]  #页面毫无规则，这是我查看的几个
    # for j in kind_page:
    for i in range(1):
        if i == 0:
            url = 'https://www.3314cc.com/Html/{}/index.html'.format('87')
        else:
            url = 'https://www.3314cc.com/Html/{}/index-{}.html'.format('87', i)
        u = get_onepage_url(url)
        URLs += u

    return URLs


# 将URLS转为list然后加上https://www.3314cc.com补全电影页面链接
# 使用生成器返回完整的电影页面链接
def bulid_filmPage_url(URLs):
    for item in URLs:
        item = list(item)
        item[0] = 'https://www.3314cc.com' + item[0]
        yield item[0]


# 获取电影的信息，下载链接
def get_down_url(url):
    # url='https://www.3314cc.com/Html/87/26945.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/68.0.3440.84 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # print(response.status_code)
    response.encoding = 'utf-8'
    pattern = re.compile(
        '<dl.*?<h1>(.*?)</h1>.*?</span>.*?<span>(.*?)</span>.*?<dd>(.*?)</dd>.*?class="downurl".*?href="(.*?)".*?>',
        re.S)
    films = re.findall(pattern, response.text)
    # print(films)
    # global number
    # number += 1  # 统计找到的电影
    return films


# 下载电影
def download_film(down_url, path):
    url = down_url[0][3]
    response_mp4 = requests.get(url, stream=True)
    content_size = int(response_mp4.headers['Content-Length']) / 1024  # 计算文件的总大小

    # 创建分类文件夹
    path_kind = path.strip('\\' + down_url[0][0] + '.mp4')
    if not os.path.exists(path_kind):  # 检验分类文件夹啊是否存在
        os.mkdir(path_kind)

    #使用progressbar显示进度条
    widgets=[down_url[0][0],    #设置当前进度条前的显示的文字
             Percentage(), '',  #显示百分比
             Bar('#'),'',       #设置进度条形状
             Timer(),'',        #显示已用时间
             ETA(),'',          #显示预计剩余时间
             FileTransferSpeed()
             ]
    progress=ProgressBar(widgets=widgets,maxval=10*content_size).start()
    print("{}开始下载....".format(down_url[0][0]))
    with open(path, 'wb') as film:
        # 实现进度条方法一，使用tqdm
        # for data in tqdm(iterable=response_mp4.iter_content(chunk_size=1024),total=content_size,unit='k'):
        for data in response_mp4.iter_content(1024):
            if data:
                film.write(data)
                progress.update(10*1024+1)
    print('下载完成！')


if __name__ == '__main__':

    URLs = get_pages_url()
    for url in bulid_filmPage_url(URLs):
        down_url = get_down_url(url)
        path = "E:\python_code\Spider_films\\{}\\{}.mp4".format(down_url[0][1], down_url[0][0])
        download_film(down_url, path)
        # path_kind = path.strip('\\'+down_url[0][0] + '.mp4')
        # print(path_kind)
        # print(path)
        # print(down_url)

    # print("共检索到{}部film".format(number))
