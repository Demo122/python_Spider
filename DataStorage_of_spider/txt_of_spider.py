#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/14 23:39
"""
import requests
from pyquery import PyQuery as pq

num=0
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = 'question: ' + item.find('h2').text()
    author = 'author: ' + item.find('.author-link-line').text()
    answer = 'answer: ' + pq(item.find('.content').html()).text().replace('\n\n','')
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()
    num+=1
print('共爬取最热话题 %d 个'%num)

# r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb：以二进制只读方式打开一个文件。文件指针将会放在文件的开头。
# r +：以读写方式打开一个文件。文件指针将会放在文件的开头。
# rb +：以二进制读写方式打开一个文件。文件指针将会放在文件的开头。
# w：以写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb：以二进制写入方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# w +：以读写方式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# wb +：以二进制读写格式打开一个文件。如果该文件已存在，则将其覆盖。如果该文件不存在，则创建新文件。
# a：以追加方式打开一个文件。如果该文件已存在，文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。
# 如果该文件不存在，则创建新文件来写入。
#
# ab：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。也就是说，新的内容将会被写入到已有内容之后。
# 如果该文件不存在，则创建新文件来写入。
#
# a +：以读写方式打开一个文件。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，则创建新文件来读写。
# ab +：以二进制追加方式打开一个文件。如果该文件已存在，则文件指针将会放在文件结尾。如果该文件不存在，则创建新文件用于读写。
