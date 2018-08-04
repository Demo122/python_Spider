#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/4 16:20
"""
# ————————————————————————————————基本实例——————————————————————————————————
# import requests

# r=requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
# 它的返回类型是requests.models.Response，响应体的类型是字符串str，Cookies的类型是RequestsCookieJar

# r=requests.get('http://httpbin.org/get')
# print(r.text)
# 构建一个最简单的GET请求，请求的链接为http://httpbin.org/get，该网站会判断如果客户端发起的是GET请求的话，它返回相应的请求信息：


# GEt请求附加额外信息，利用params参数
# data={
#     'name':'germey',
#     'age':22
# }
# r=requests.get('http://httpbin.org/get',params=data)
# print(r.text)

# r = requests.get('http://httpbin.org/get')
# print(type(r.text)) # 返回结果是json格式的字符串
# print(r.json())     # 调用json()方法将返回结果是json格式的字符串转化为字典
# print(type(r.json()))
# 需要注意。如果返回结果不是json格式便会报错，抛出json.decoder.JSONDecoderError异常


# ---------------------------------抓取网页-------------------------
# 上面的请求链接返回的是JSON形式的字符串，那么如果请求普通的网页，则肯定能获得相应的内容了。下面以“知乎”→“发现”页面为例来看一下
# import requests
# import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)  # 书本中
# # pattern=re.compile(r'<.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, r.text)
# print(titles)


# -------------------------------抓取二进制数据----------------------
# 图片、音频、视频这些文件本质上都是由二进制码组成的,想要抓取它们，就要拿到它们的二进制码。
# 下面以GitHub的站点图标为例来看一下
# import requests
#
# r=requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico','wb') as f:
#     f.write(r.content)


# --------------------------------添加headers-------------------------
# 与urllib.request一样，我们也可以通过headers参数来传递头信息。
# 比如，在上面“知乎”的例子中，如果不传递headers，就不能正常请求
# 但如果加上headers并加上User - Agent信息，那就没问题了：
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 '
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)
#
# 我们可以在headers这个参数中任意添加其他的字段信息。


# --------------------------------POST请求----------------------------
# 这里还是请求http://httpbin.org/post，该网站可以判断如果请求是POST方式，就把相关请求信息返回。
# import requests
#
# data = {'name': 'mike', 'age': '22'}
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# ------------------------------------响应------------------------------
# 发送请求后，得到的自然就是响应。在上面的实例中，我们使用text和content获取了响应的内容。
# 此外，还有很多属性和方法可以用来获取其他信息，比如状态码、响应头、Cookies等
# import requests
#
# r=requests.get('http://www.jianshu.com')
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.url),r.url)
# print(type(r.history),r.history)


# 状态码常用来判断请求是否成功，而requests还提供了一个内置的状态码查询对象requests.codes
import requests

headers={
    'User-Agent':'Mozilla/5.0'
}
r = requests.get('http://www.jianshu.com',headers=headers)
exit() if not r.status_code == requests.codes.ok else print('Request Successfully!')
