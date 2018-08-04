#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/4 15:35
"""

# robots.txt样例

# 1.对所有搜索爬虫只允许爬取public目录
# User-agent: *     User-agent描述了搜索爬虫的名称，这里将其设置为*则代表该协议对任何爬取爬虫有效
# Disallow:/        Disallow指定了不允许抓取的目录，比如上例子中设置为/则代表不允许抓取所有页面。
# Allow:/public/    Allow一般和Disallow一起使用，一般不会单独使用，用来排除某些限制。
#                   现在我们设置为/public/，则表示所有页面不允许抓取，但可以抓取public目录。

# 只允许摸一个爬虫访问的代码如下
# User-agent:WebCrawler
# Disallow:
# User-agent:*
# Disallow:/

# 禁止所有爬虫访问某些目录
# User-agent:*
# Disallow:/private/
# Disallow:/tmp/

# 类RobotFileParser，它可以根据某网站的robots.txt文件来判断一个爬取爬虫是否有权限来爬取这个网页。
# set_url()：用来设置robots.txt文件的链接。如果在创建RobotFileParser对象时传入了链接，那么就不需要再使用这个方法设置了

# read()：读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析操作，如果不调用这个方法，接下来的判断都会为False，
# 所以一定记得调用这个方法。这个方法不会返回任何内容，但是执行了读取操作。

# parse()：用来解析robots.txt文件，传入的参数是robots.txt某些行的内容，它会按照robots.txt的语法规则来分析这些内容。

# can_fetch()：该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。返回的内容是该搜索引擎是否可以抓取这个URL，
# 返回结果是True或False。

# mtime()：返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫是很有必要的，你可能需要定期检查来抓取最新的robots.txt。

# modified()：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和分析robots.txt的时间。

# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

# 也可以用parse()方法执行读取和分析
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen,Request

rp = RobotFileParser()
headers={
    'User-Agent':'Mozilla/4.0(compatible;MSIE 5.5;windows NT)'
}
rep=Request(url='http://www.jianshu.com/robots.txt',headers=headers)
rp.parse(urlopen(rep).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

