#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/5 14:27
"""

# --------------------------------文件上传---------------------------------
# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)
# {"file": "data:application/octet-stream;base64,AAAAAA...=" }
# 这个网站会返回响应，里面包含files这个字段，而form字段是空的，这证明文件上传部分会单独有一个files字段来标识。


# --------------------------------Cookies----------------------------------
# import requests
#
# r=requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)
# 用items()方法将其转化为元组组成的列表，遍历输出每一个Cookie的名称和值，实现Cookie的遍历解析

# 用Cookie来维持登录状态，以知乎为例
# import requests

# headers={
#     'Cookie':'_zap=d7b89bb0-03aa-46a2-be24-32a76db1b0af;'
#              ' d_c0="APBlkVknAQ6PTvoGHlBd93UTDm-CO_aGVpU=|1533375592"; '
#              'q_c1=2324b2f2490349678d5e476b5ccdc3e4|1533375628000|1533375628000;'
#              ' __utma=51854390.353456779.1533375633.1533375633.1533375633.1;'
#              ' __utmz=51854390.1533375633.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/;'
#              ' __utmv=51854390.000--|3=entry_date=20180804=1;'
#              ' l_cap_id="NDVmMTBiNGUxZDQ5NDIyYTllN2M5NzMzMzc0YTVkOWM=|1533377284|1a3b205f39548e6e2ce993ee33e61be0491b1f45";'
#              ' r_cap_id="NWMzZWJkYTVhOGQxNDU1N2E4MzYxMWYxNjI2NzljMDU=|1533377284|d41660424df38d3c16d43bb7cd743e21d2f8ed1c";'
#              ' cap_id="ZjU4OTcyOWJlOTFiNDRjMTljMTJjMjcwYmY1Y2U3YWM=|1533377284|64372383294f751dbfb30b8209f697f6c9b85b88"; '
#              'tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; _xsrf=ac3e28ad-8c28-4e4c-9d59-05a8c42decc5;'
#              ' capsion_ticket="2|1:0|10:1533452658|14:capsion_ticket|44:OWU0NjI2YmYxNTAyNDNiNWJjMzc0ZTJjNzNmNmY4NDk=|33e6fe9e6c2fc4787044b6170e34a2c801a1dd353b0f20a98e851ef06fa59ba2";'
#              ' z_c0="2|1:0|10:1533452696|4:z_c0|92:Mi4xTFBDVUJ3QUFBQUFBOEdXUldTY0JEaVlBQUFCZ0FsVk5tTzlUWEFBTlRtd1pyQ2x4RjcxVE1zX0UwTGZVSXZVUFZn|455fe3c1dd0ee6ab789cea48f1aa16737889b2da372634961ff29bc21f58d1c7";'
#              ' unlock_ticket="AEBs5eL-EQ0mAAAAYAJVTaCoZls0jdwfloVTCYdBg0fWvfiB8LtCzg=="',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0'
# }
# r=requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

# 也可以通过cookies参数来设置，这样需要构造RequestsCookieJar对象，而且需要分割一下cookies
# cookies='_zap=d7b89bb0-03aa-46a2-be24-32a76db1b0af; d_c0="APBlkVknAQ6PTvoGHlBd93UTDm-CO_aGVpU=|1533375592";' \
#         ' q_c1=2324b2f2490349678d5e476b5ccdc3e4|1533375628000|1533375628000;' \
#         '__utma=51854390.353456779.1533375633.1533375633.1533375633.1;' \
#         ' __utmz=51854390.1533375633.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/;' \
#         ' __utmv=51854390.000--|3=entry_date=20180804=1; ' \
#         'l_cap_id="NDVmMTBiNGUxZDQ5NDIyYTllN2M5NzMzMzc0YTVkOWM=|1533377284|1a3b205f39548e6e2ce993ee33e61be0491b1f45";' \
#         ' r_cap_id="NWMzZWJkYTVhOGQxNDU1N2E4MzYxMWYxNjI2NzljMDU=|1533377284|d41660424df38d3c16d43bb7cd743e21d2f8ed1c"; ' \
#         'cap_id="ZjU4OTcyOWJlOTFiNDRjMTljMTJjMjcwYmY1Y2U3YWM=|1533377284|64372383294f751dbfb30b8209f697f6c9b85b88";' \
#         ' tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; _xsrf=ac3e28ad-8c28-4e4c-9d59-05a8c42decc5;' \
#         ' capsion_ticket="2|1:0|10:1533452658|14:capsion_ticket|44:OWU0NjI2YmYxNTAyNDNiNWJjMzc0ZTJjNzNmNmY4NDk=|33e6fe9e6c2fc4787044b6170e34a2c801a1dd353b0f20a98e851ef06fa59ba2"; ' \
#         'z_c0="2|1:0|10:1533452696|4:z_c0|92:Mi4xTFBDVUJ3QUFBQUFBOEdXUldTY0JEaVlBQUFCZ0FsVk5tTzlUWEFBTlRtd1pyQ2x4RjcxVE1zX0UwTGZVSXZVUFZn|455fe3c1dd0ee6ab789cea48f1aa16737889b2da372634961ff29bc21f58d1c7";' \
#         ' unlock_ticket="AEBs5eL-EQ0mAAAAYAJVTaCoZls0jdwfloVTCYdBg0fWvfiB8LtCzg=="'
# jar=requests.cookies.RequestsCookieJar()
# headers={
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozila/5.0'
# }
# for cookie in cookies.split(';'):
#     key,value=cookie.split('=',1)
#     jar.set(key,value)
# r=requests.get('https://www.zhihu.com',cookies=jar,headers=headers)
# print(r.text)

# 首先新建了一个RequestCookieJar对象，然后将复制下来的cookies利用split()方法分割
# ，接着利用set()方法设置好每个Cookie的key和value，然后通过调用requests的get()方法并传递给cookies参数即可。
# 当然，由于知乎本身的限制，headers参数也不能少，只不过不需要在原来的headers参数里面设置cookie字段了


# ----------------------------------会话维持--------------------------
# import requests
#
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r=requests.get('http://httpbin.org/cookies')
# print(r.text)
# 这里我们请求了一个测试网址http://httpbin.org/cookies/set/number/123456789。
# 请求这个网址时，可以设置一个cookie，名称叫作number，内容是123456789，
# 随后又请求了http://httpbin.org/cookies，此网址可以获取当前的Cookies。
# 结果如下
# {
#   "cookies": {}
# }

# 使用Session 维持同一个会话
# import requests
#
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
# 结果如下
# {
#   "cookies": {
#     "number": "123456789"
#   }
# }
# 利用Session，可以做到模拟同一个会话而不用担心Cookies的问题。它通常用于模拟登录成功之后再进行下一步的操作。
# Session在平常用得非常广泛，可以用于模拟在一个浏览器中打开同一站点的不同页面


# ----------------------------SSL证书验证---------------------
# import logging
# import requests
# from requests.packages import urllib3
#
# urllib3.disable_warnings()         #我们可以通过设置忽略警告的方式来屏蔽这个警告
# #logging.captureWarnings(True)     # 或者通过捕获警告到日志的方式忽略警告
# r = requests.get('https://www.12306.cn',verify=False)   #参数verify默认为True，改为False设置忽略证书验证
# #也可以指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组：
# #response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# #上面的代码是演示实例，我们需要有crt和key文件，并且指定它们的路径。注意，本地私有证书的key必须是解密状态，加密状态的key是不支持的。
# print(r.status_code)


# -----------------------------代理设置------------------------
# import requests
#
# # 若代理需要使用HTTP Basic Auth，可以使用类似http://user:password@host:port这样的语法来设置代理
# proxies = {
#      "http": "http://user:password@10.10.1.10:3128/",
# }
# r = requests.get('https://www.taobao.com', proxies=proxies)
# print(r.text)

# 除了基本的HTTP代理外，requests还支持SOCKS协议的代理。
# 示例如下
# import requests
#
# proxies = {
#      'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port',
# }
# r=requests.get("https://www.taobao.com", proxies=proxies)
# print(r.text)


# ----------------------------超时设置---------------------
# import requests
#
# r = requests.get("http://www.taobao.com", timeout=10)
# print(r.status_code)
# 实际上，请求分为两个阶段，即连接（connect）和读取（read）。
# 上面设置的timeout将用作连接和读取这二者的timeout总和
# 如果要分别指定，就可以传入一个元组：
# r = requests.get('https://www.taobao.com', timeout=(5, 11, 30))
# 如果想永久等待，可以直接将timeout设置为None，或者不设置直接留空，因为默认是None


# -----------------------------身份认证----------------------
# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('usename', 'password'))
# requests提供了一个更简单的写法，可以直接传一个元组，它会默认使用HTTPBasicAuth这个类来认证
# # r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)
# 果用户名和密码正确的话，请求时就会自动认证成功，会返回200状态码，如果认证失败，则返回401状态码。


# 此外，requests还提供了其他认证方式，如OAuth认证，不过此时需要安装oauth包
# pip3 install requests_oauthlib
# 使用OAuth1认证的方法如下
# import requests
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)


#------------------------------Prepared Request-------------------
#urllib时，我们可以将请求表示为数据结构，其中各个参数都可以通过一个Request对象来表示。
#这在requests里同样可以做到，这个数据结构就叫Prepared Reques
from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

#这里我们引入了Request，然后用url、data和headers参数构造了一个Request对象，
# 这时需要再调用Session的prepare_request()方法将其转换为一个Prepared Request对象，然后调用send()方法发送即可

#有了Request这个对象，就可以将请求当作独立的对象来看待，这样在进行队列调度时会非常方便