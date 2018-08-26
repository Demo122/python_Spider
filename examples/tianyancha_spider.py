#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/26 17:07
"""

from pyquery import PyQuery
from urllib.parse import urlencode
import requests

def search_page(wd):
    headers={
        'Cookie':'TYCID=5f4dca50a90e11e8af52a178390b50c0;'
                  ' undefined=5f4dca50a90e11e8af52a178390b50c0;ssuid=8950861696; _ga=GA1.2.865980201.1535273985; '
                  '_gid=GA1.2.1676428516.1535273985; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1535277942,1535278021; '
                  'tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3OTY2OTQyNiIsImlhdCI'
                  '6MTUzNTI3NzgzMywiZXhwIjoxNTUwODI5ODMzfQ.1UFXQcKOfOj0jwuvMfF2sEbHPYaO2kyJuXN-2nqBB38eagHk70zvS5BMOW8a'
                  'a14bqtTFtRvdkVq7u3pYMCVzSA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A'
                  '%25220%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%252'
                  '2vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252218879669'
                  '426%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODg3OTY2OTQyNiIsImlhdCI6MTUzNTI3NzgzMywiZ'
                  'XhwIjoxNTUwODI5ODMzfQ.1UFXQcKOfOj0jwuvMfF2sEbHPYaO2kyJuXN-2nqBB38eagHk70zvS5BMOW8aa14bqtTFtRvdkVq7u3p'
                  'YMCVzSA; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1535278111',
        'Host':'www.tianyancha.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url='https://www.tianyancha.com/search?'+urlencode({'key':wd})
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(e.args)
        return None

def parse_html(page):
    doc=PyQuery(page)
    items=doc('.result-list').items()
    for item in items:
        text=item.text().replace('查看更多','')





if __name__=='__main__':
    wd='深圳公司'
    page=search_page(wd)
    parse_html(page)

