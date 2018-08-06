#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/6 13:32
"""
import requests
import re

headers={
    'Cookie':'ASPSESSIONIDSAASTAQS=BFILPOHDOHBOMGDNECFINHMJ; OpenWindow=; CurrQzjiaowuLoginLb=xs; LoginLb=xs',
    'Host':'218.65.59.52',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'

}
r=requests.get('http://218.65.59.52/jwxs/Xsxk/default.asp?Datetime=2018-8-6%2014:22:26',headers=headers)
#如果 Requests 检测不到正确的编码，那么你告诉它正确的是什么：
# response.encoding = 'gbk'
# print(response.text)

r.encoding='gbk'
# pattern=re.compile(r'<option.*?>(.*?)</option>',re.S)
# s=re.findall(pattern,r.text.encode(r.encoding).decode('gbk'))
# print(s)
# print(type(s[1]))

print(r.text)
