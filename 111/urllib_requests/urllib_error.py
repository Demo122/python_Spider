#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/2 21:16
"""

import socket
from urllib import request, error

# URLError
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.URLError as e:
#     print(e.reason)


# HTTPError
# try:
#     response=request.urlopen('http://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')


# 因为URLError是HTTPError的父类，所以可以先选择捕获子类的错误，再去捕获父类的错误
# try:
#     response = request.urlopen('http://cuiqingcai.com/index.html')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully!')


#有时候，reason属性返回的不一定是字符串，也可能是一个对象
try:
    response=request.urlopen('http://www.baidu.com',timeout=0.01)
except error.URLError as e:
    print(type(e.reason))  #<class 'socket.timeout'>
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT!")