#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/2 23:25
"""

import socket
import urllib.request
import urllib.parse
import urllib.error

# urlopen
# response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))
# print(response.status) #响应状态吗
# print(response.getheaders()) #打印头信息
# print(response.getheader('Server')) #获取响应头中的Server值


# data
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# respone = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(respone.read())


# timeout
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

#urlopen()还有context参数，它必须是ssl。SSLContext类型，用来指定SSL设置
#此外，cafile和capath这两个参数分别指定CA证书和它的路径，这个在请求HTTPS链接时会有用
#cadefault参数已经弃用了，其默认值为False