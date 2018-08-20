#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/20 16:42
"""

# from collections import Iterable
import time
from multiprocessing.pool import Pool
from hashlib import md5
from urllib.parse import urlencode
import requests
import os


def get_page(offset):
    base_url = 'https://www.toutiao.com/search_content/?'
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'form': 'search_tab'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        return None


def get_image_url(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title'):
                title = item.get('title')
                for image in item.get('image_list'):
                    yield {
                        'title': title,
                        'image_url': image.get('url')
                    }


def save_images(item):
    base_path='./街拍美图/'+item.get('title')
    if not os.path.exists('./街拍美图'):
        os.mkdir('./街拍美图')
    if not os.path.exists(base_path):
        os.mkdir(base_path)  # 创建图片文件夹
    try:
        response = requests.get('https:'+item.get('image_url'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(base_path, md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download to ', file_path)
    except requests.ConnectionError:
        print('Failed to save images!')


def main(offset):
    json = get_page(offset)
    for item in get_image_url(json):
        save_images(item)


GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    time_start = time.time()
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

    # for offset in range(0,400,20):
    #     main(offset)
    time_end=time.time()
    print('共耗时：',time_end-time_start)