#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/2 22:15
"""

# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(type(result), result)

# 可以得出一个标准的链接格式
# scheme://netloc/path;parameters?query#fragment

# urlparse()方法还有其他配置吗？接下来，看一下它的API用法
# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# urlstring：这是必填项，即待解析的URL。
# scheme：它是默认的协议（比如http或https等）。假如这个链接没有带协议信息，会将这个作为默认的协议。
# allow_fragments：即是否忽略fragment。如果它被设置为False，fragment部分就会被忽略，
# 它会被解析为path、parameters或者query的一部分，而fragment部分为空


# ParseResult实际上是一个元组，我们可以用索引顺序来获取，也可以用属性名获取

# urlunparse()
# from urllib.parse import urlunparse
#
# data = ('http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment')
# print(urlunparse(data))
# 用此方法构造URL
# http://www.baidu.com/index.html;user?a=6#comment
# urlunparse()接受一个可迭代对象，长度必须是6，否则会抛出参数数量不足或者过多的问题


# urlsplit()
# 这个方法和urlparse()类似，只不过不再单独解析params部分，只返回5个结果，把params合并到path中
# from urllib.parse import urlsplit
#
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
# SplitResult(scheme='http', netloc='www.baidu.com', path='/index.html;user', query='id=5', fragment='comment')
# SplitResult是一个元祖类型，既可以用属性获取值也可以用索引来获取


# urlunsplit()
# 和urlunparse()类型，区别是参数长度必须为5
# from urllib.parse import urlunsplit
#
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))
# http://www.baidu.com/index.html?a=6#comment


# urljoin()
# 向该方法提供一个base_url(基础连接)作为第一个参数，将新链接作为第二个参数
# 该方法会分析base_url的scheme,netloc,path这三个内容并对新链接缺失的部分进行补充,最后返回结果
# from urllib.parse import urljoin
#
# print(urljoin('http://wwww.baidu.com', 'FAQ.html'))
# print(urljoin('http://wwww.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://wwww.baicu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://wwww.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# print(urljoin('http://wwww.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))
# base_url提供了三项内容scheme，netloc，path。如果这三项在新的链接里不存在，就予以补充，
# 如果新链接存在，就使用新链接部分，而base_url中的params，query，fragment是不起作用的


# urlencode()
# 构造GET请求参数很有用，首先声明一个字典来表示参数，然后调用urlencode()将其序列化为GEt请求参数
# from urllib.parse import urlencode
#
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)
# http://www.baidu.com?name=germey&age=22


# parse_qs()
# 反序列化，利用parse_qs()方法可将一串GET请求参数转回字典
# from urllib.parse import parse_qs
#
# query = 'name=germey&age=22'
# print(parse_qs(query))
# {'name': ['germey'], 'age': ['22']}


# parse_qsl()
# 它用于将参数转化为元组组成的列表
# from urllib.parse import parse_qsl
#
# query = 'name=germey&age=22'
# print(parse_qsl(query))
# [('name', 'germey'), ('age', '22')]


# quote()
# 该方法可以将内容转化为URL编码的格式，URL中带有中文参数时，有时可能会导致乱码的问题，
# 这个方法可以将中文字符转化为URL编码
# from urllib.parse import quote
#
# keyword = '壁纸'
# url = 'http://www.baidu.com/s?wd=' + quote(keyword)
# print(url)
# http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8


# unquote()
# 进行URL解码
import re
from urllib.parse import unquote, urlparse

url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(url)
# http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8

result = urlparse(unquote(url))
keyword = result.query
m = re.match(r'wd=(.*)', keyword)
print(m.group(1))
