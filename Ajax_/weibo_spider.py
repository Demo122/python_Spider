#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/19 22:36
"""

# from pymongo import MongoClient

from collections import Iterable
from pyquery import PyQuery as pq
from urllib.parse import urlencode
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    # 'Refer': 'https://m.weibo.cn/u/2830678474',
    'Reder':'https://m.weibo.cn/p/1005055189576388',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        # 'type': 'uid',
        # 'value': '2830678474',
        'containerid': '1076035189576388',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if isinstance(item,Iterable):
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['created_at'] = item.get('created_at')
                weibo['text'] = pq(item.get('text')).text()  # 使用pyquery将正文中的HTML标签去掉
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


# 我们还可以加一个方法将结果保存到MongoDB数据库
# def save_to_mongo(result):
#     if collection.insert(result):
#         print('Saved to Mongo')


if __name__ == '__main__':
    # client = MongoClient()
    # db = client['weibo']
    # collection = db['weibo']
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            # save_to_mongo(result)
