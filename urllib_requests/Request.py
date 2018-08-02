#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/2 14:23
"""
# 如果请求中需要加入Headers等信息，就可以利用更强大的Request类来构建

# Request例子
# import urllib.request
# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


# 传入多个参数构建请求
# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
#
# # req=request.Request(url=url,data=data,headers=headers,method='POST')
# # 另外，headers也可以用add_header（）的方法来添加
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)')
#
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


# 验证
# 有些网站在打开时会弹出提示框，要求输入用户名和密码，验证成功后才能查看页面
# 要请求这样的页面，需要借助HTTPBasicAuthHandler
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'  # 测试网页
#
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
#
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# 代理  添加代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)
# 在本地搭建了一个代理，运行在9743端口
# Proxy_Handler的参数是一个字典，键名是协议类型，键值是代理链接，可以添加多个代理


# Cookies
import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + " = " + item.value)

# 将cookies以文件格式保存
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# 从文件中读取利用cookies
cookie = http.cookiejar.MozillaCookieJar()
cookie.load('cookies.txt',ignore_expires=True,ignore_discard=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
