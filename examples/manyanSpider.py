#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/6 21:31
"""
import requests
import re
import json
import time
from requests.exceptions import RequestException


# 抓取首页
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/68.0.3440.84 Safari/537.36'
    }
    try:
        respone = requests.get(url, headers=headers)
        if respone.status_code == 200:
            return respone.text
        return None
    except RequestException:
        return None


# 正则提取
def parse_one_page(html):
    pattern = re.compile(
        '<dd.*?board-index.*?(\d+).*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>\s+(.*?)\s+</p>'
        '.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    titles = re.findall(pattern, html)
    for item in titles:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3],
            'releasetime': item[4],
            'score': item[5] + item[6]
        }


# 写入文件
def write_to_file(content):
    with open('maoyan_movies_top100.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    # for i in parse_one_page(html):
    #     print(type(j))
    for content in parse_one_page(html):
        write_to_file(content)


if __name__ == '__main__':
    # 分页爬取，修改offset的偏移量
    for i in range(10):
        main(i * 10)
        time.sleep(1)  # 猫眼多了反爬虫，如果速度过快则会无响应，所有增加一个延时等待
