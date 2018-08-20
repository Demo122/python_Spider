#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/20 16:42
"""

from collections import Iterable
from urllib.parse import urlencode
import requests

def get_page(offset):
    base_url='https://www.toutiao.com/search_content/?'
    params={
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'cur_tab':1,
        'form':'search_tab'
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        return None

def get_image_url(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('title'):
                title=item.get('title')
                print(title)
                for image in item.get('image_list'):
                    yield {
                        'title':title,
                        'image_url':image.get('url')
                    }


if __name__=='__main__':
    page=get_page(0)
    for i in get_image_url(page):
        print(i)