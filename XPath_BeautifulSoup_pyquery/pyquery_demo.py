#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/14 13:55
"""
from pyquery import PyQuery as pq

# -----------------------------初始化-------------------------
# 像Beautiful Soup一样，初始化pyquery的时候，也需要传入HTML文本来初始化一个PyQuery对象。
# 它的初始化方式有多种，比如直接传入字符串，传入URL，传入文件名

# 字符串初始化
# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# doc=pq(html)
# print(doc('li'))  #将初始化的对象传入CSS选择器 我们传入li节点，这样就可以选择所有的li节点。

# URL初始化
# 此时只需要指定参数为url
# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))
# PyQuery对象会首先请求这个URL，然后用得到的HTML内容完成初始化，这其实就相当于用网页的源代码以字符串的形式传递给PyQuery类来初始化
# 它与下面的功能是相同的
# import requests
# doc = pq(requests.get('http://cuiqingcai.com').text)
# print(doc('title'))

# 文件初始化
# 将参数指定为filename即可
# doc=pq(filename='test.html')
# print(doc('li'))


# -------------------------- 基本CSS选择器--------------------
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# doc=pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))
# 类型依然是PyQuery类型。


# -------------------------- 查找节点--------------------------
#下面我们介绍一些常用的查询函数，这些函数和jQuery中函数的用法完全相同。
#子节点
#查找子节点时，需要用到find()方法，此时传入的参数是CSS选择器 这里还是以前面的HTML为例：
# doc = pq(html)
# items = doc('.list')
# # print(type(items))
# # print(items)
# # lis = items.find('li')
# # print(type(lis))
# # print(lis)
#
# #其实find()的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那么可以用children()方法：
# lis=items.children()
# # print(type(lis))
# # print(lis)
# #如果要筛选所有子节点中符合条件的节点，比如想筛选出子节点中class为active的节点，可以向children()方法传入CSS选择器.active：
# print(items.children('.active'))

#父节点
#用parent()方法来获取某个节点的直接父节点
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc=pq(html)
# items=doc('.list')
# container=items.parent()
# print(type(container))
# print(container)

#获取某个祖先节点，用parents()方法,parents()方法会返回所有的祖先节点。
# container=items.parents()
# print(container)

#如果想要筛选某个祖先节点的话，可以向parents()方法传入CSS选择器，这样就会返回祖先节点中符合CSS选择器的节点：
# container=items.parents('.wrap')
# print(container)

#兄弟节点
#要获取兄弟节点，可以使用siblings()方法 这里还是以上面的HTML代码为例：
# doc=pq(html)
# li=doc('.item-0.active')
# print(li.siblings())

#如果要筛选某个兄弟节点，我们依然可以向siblings方法传入CSS选择器，
# print(li.siblings('.active'))


#----------------------------- 遍历-------------------------------
#pyquery的选择结果可能是多个节点，也可能是单个节点，类型都是PyQuery类型
#我们就需要遍历来获取了。例如，这里把每一个li节点进行遍历，需要调用items()方法
# doc = pq(html)
# lis = doc('li').items() #调用items()方法后，会得到一个生成器
# print(type(lis))
# for li in lis:
#     print(li, type(li))


#----------------------------获取信息--------------------------
#获取属性
#提取到某个PyQuery类型的节点后，就可以调用attr()方法来获取属性
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# #然后调用attr()方法。在这个方法中传入属性的名称，就可以得到这个属性值了。
# print(a.attr('href'))  # link3.html
# #也可以通过调用attr属性来获取属性，用法如下
# print(a.attr.href)     # link3.html

#当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性。
#需要获取多个选中多个节点的属性，需要使用遍历
# doc=pq(html)
# list_a=doc('a').items()
# for a in list_a:
#     print(a.attr.href)
#在进行属性获取时，可以观察返回节点是一个还是多个，如果是多个，则需要遍历才能依次获取每个节点的属性

#获取文本
#获取节点之后的另一个主要操作就是获取其内部的文本了，此时可以调用text()方法来实现
# doc=pq(html)
# li=doc('.item-0.active a')
# print(li)
# print(li.text())
# #但如果想要获取这个节点内部的HTML文本，就要用html()方法
# print(li.html())

#如果我们选中的结果是多个节点，text()或html()会返回什么内容？html()方法返回的是第一个li节点的内部HTML文本，
# 而text()则返回了所有的li节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串


#如果得到的结果是多个节点，并且想要获取每个节点的内部HTML文本，则需要遍历每个节点。
# 而text()方法不需要遍历就可以获取，它将所有节点取文本之后合并成一个字符串


#-----------------------------节点操作-----------------------
#addClass和removeClass
#addClass()和removeClass()这些方法可以动态改变节点的class属性。
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)
#结果
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-0"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>

#attr、text和html
# #如果attr()方法只传入第一个参数的属性名，则是获取这个属性值；如果传入第二个参数，可以用来修改属性值。
# text()和html()方法如果不传参数，则是获取节点内纯文本和HTML文本；如果传入参数，则进行赋值
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)
#结果
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-0 active" name="link"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-0 active" name="link">changed item</li>
# <li class="item-0 active" name="link"><span>changed item</span></li>

#remove()
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
# print(wrap.text())
#现在想提取Hello, World这个字符串，而不要p节点内部的字符串，首先选中p节点，
#调用了remove()方法将其移除，然后这时wrap内部就只剩下Hello, World这句话了，然后再利用text()方法提取即可
wrap.find('p').remove()
print(wrap.text())


#---------------------- 伪类选择器---------------------
#CSS选择器之所以强大，还有一个很重要的原因，那就是它支持多种多样的伪类选择器
# # ，例如选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点等。示例如下：
# html = '''
# <div class="wrap">
#     <div id="container">
#         <ul class="list">
#              <li class="item-0">first item</li>
#              <li class="item-1"><a href="link2.html">second item</a></li>
#              <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#              <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#              <li class="item-0"><a href="link5.html">fifth item</a></li>
#          </ul>
#      </div>
#  </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc('li:first-child')
# print(li)
# li = doc('li:last-child')
# print(li)
# li = doc('li:nth-child(2)')
# print(li)
# li = doc('li:gt(2)')
# print(li)
# li = doc('li:nth-child(2n)')
# print(li)
# li=doc('li:contains(second)')
# print(li)
#这里我们使用了CSS3的伪类选择器，依次选择了第一个li节点、最后一个li节点、第二个li节点、
# 第三个li之后的li节点、偶数位置的li节点、包含second文本的li节点。