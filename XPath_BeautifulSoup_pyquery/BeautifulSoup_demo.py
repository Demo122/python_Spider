#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/12 17:06
"""

# 测试
# from bs4 import BeautifulSoup
# soup=BeautifulSoup('<p>Hello!</p>','lxml')
# print(soup.p.string)
#如果节点内再无其他子节点，则可以通过string属性来获取其中的文本内容

from bs4 import BeautifulSoup

# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# ----------------------------基本用法-------------------------
# 下面首先用实例来看看Beautiful Soup的基本用法：
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
# # 调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出。
# # 这里需要注意的是，输出结果里面包含body和html节点，也就是说对于不标准的HTML字符串BeautifulSoup，可以自动更正格式。
# # 这一步不是由prettify()方法做的，而是在初始化BeautifulSoup时就完成了
# print(soup.title.string)
# # 然后调用soup.title.string，这实际上是输出HTML中title节点的文本内容。
# # 所以，soup.title可以选出HTML中的title节点，再调用string属性就可以得到里面的文本了


# ----------------------------节点选择器----------------------
# 选择元素
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)             # <title>The Dormouse's story</title>
# print(type(soup.title))       # <class 'bs4.element.Tag'>
# print(soup.title.string)      # The Dormouse's story
# print(soup.head)              # <head><title>The Dormouse's story</title></head>
# print(soup.p)                 # <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# 首先打印输出title节点的选择结果，输出结果正是title节点加里面的文字内容。
# 接下来，输出它的类型，是bs4.element.Tag类型，这是Beautiful Soup中一个重要的数据结构。
# 经过选择器选择后，选择结果都是这种Tag类型。Tag具有一些属性，
# 比如string属性，调用该属性，可以得到节点的文本内容，所以接下来的输出结果正是节点的文本内容。
# 当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略。


#提取信息
#(1)获取名称  可以利用name属性获取节点的名称
# soup=BeautifulSoup(html,'lxml')
# print(soup.title.name)  #title

#(2)获取属性   每个节点可能有多个属性，比如id和class等，选择这个节点元素后，可以调用attrs获取所有属性
# print(soup.p.attrs)             # {'class': ['title'], 'name': 'dromouse'}
# print(soup.p.attrs['name'])     # dromouse
#可以不用写attrs，直接在节点元素后面加中括号，传入属性名就可以获取属性值了
# print(soup.p['class'])      # ['title']
# print(soup.p['name'])       # dromouse

#(3)获取内容  可以利用string属性获取节点元素包含的文本内容
# print(soup.p.string)   #The Dormouse's story
#再次注意一下，这里选择到的p节点是第一个p节点，获取的文本也是第一个p节点里面的文本。


#嵌套选择
#每一个返回结果都是bs4.element.Tag类型，它同样可以继续调用节点进行下一步的选择
# itle.string)     # The Dormouse's storyhtml = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# """
# soup=BeautifulSoup(html,'lxml')
# print(soup.head.title)            # <title>The Dormouse's story</title>
# print(type(soup.head.title))      # <class 'bs4.element.Tag'>
# print(soup.head.t


#关联选择
#(1)子节点和子孙节点
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.contents)
#返回结果是列表形式。p节点里既包含文本，又包含节点，最后会将它们以列表形式统一返回
#contents属性得到的结果是直接子节点的列表

#可以调用children属性得到相应的结果
# print(soup.p.children)      #调用了children属性来选择，返回结果是生成器类型
# for i,child in enumerate(soup.p.children):
#     #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
#     print(i,child)

#得到所有的子孙节点的话，可以调用descendants属性
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)
#返回结果还是生成器。遍历输出一下可以看到，这次的输出结果就包含了span节点。descendants会递归查询所有子节点，得到所有的子孙节点。

#(2)父节点和祖先节点
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#         </p>
#         <p class="story">...</p>
# """
# soup=BeautifulSoup(html,'lxml')
# print(soup.a.parent)
#这里输出的仅仅是a节点的直接父节点，而没有再向外寻找父节点的祖先节点。如果想获取所有的祖先节点，可以调用parents属性
# html = """
# <html>
#     <body>
#         <p class="story">
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#         </p>
# """
# soup=BeautifulSoup(html,'lxml')
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))
#返回结果是生成器类型 这里用列表输出了它的索引和内容，而列表中的元素就是a节点的祖先节点。

#(3)兄弟节点
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             Hello
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
# """
# soup=BeautifulSoup(html,'lxml')
# print('Next Sibling',soup.a.next_sibling)
# print('Prev sibling',soup.a.previous_sibling)
# print('Next siblings',list(enumerate(soup.a.next_siblings)))
# print('prev siblings',list(enumerate(soup.a.previous_siblings)))
# 这里调用了4个属性，其中next_sibling和previous_sibling分别获取节点的下一个和上一个兄弟元素，
# next_siblings和previous_siblings则分别返回所有前面和后面的兄弟节点的生成器。

#(4)提取信息
# html = """
# <html>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">Bob</a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#         </p>
# """
# soup = BeautifulSoup(html, 'lxml')
# print('Next Sibling:')
# print(type(soup.a.next_sibling))
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.string)
# print('Parent:')
# print(type(soup.a.parents))
# print(list(soup.a.parents)[0])
# print(list(soup.a.parents)[0].attrs['class'])
#如果返回结果是单个节点，那么可以直接调用string、attrs等属性获得其文本和属性；
# 如果返回结果是多个节点的生成器，则可以转为列表后取出某个元素，然后再调用string、attrs等属性获取其对应节点的文本和属性


#---------------------------方法选择器--------------------------
#find_all()
# 顾名思义，就是查询所有符合条件的元素。给它传入一些属性或文本，就可以得到符合条件的元素，它的功能十分强大
#它的API如下：
# find_all(name , attrs , recursive , text , **kwargs)

#(1)name
# 我们可以根据节点名来查询元素，示例如下：
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))
#这里我们调用了find_all()方法，传入name参数，其参数值为ul。也就是说，我们想要查询所有ul节点，返回结果是列表类型，长度为2，
# 每个元素依然都是bs4.element.Tag类型

# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#因为都是Tag类型，所以依然可以进行嵌套查询。还是同样的文本，这里查询出所有ul节点后，再继续查询其内部的li节点：

# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)
#返回结果是列表类型，列表中的每个元素依然还是Tag类型。
# 接下来，就可以遍历每个li，获取它的文本了

#2)attrs
# 除了根据节点名查询，我们也可以传入一些属性来查询，示例如下：
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))

#对于一些常用的属性，比如id和class等，我们可以不用attrs来传递。比如，要查询id为list-1的节点，可以直接传入id这个参数。
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_='element'))
#返回的结果依然还是Tag组成的列表。

#(3)text
#text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象，示例如下
# import re
# html='''
# <div class="panel">
#     <div class="panel-body">
#         <a>Hello, this is a link</a>
#         <a>Hello, this is a link, too</a>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link'))) #['Hello, this is a link', 'Hello, this is a link, too']
#结果返回所有匹配正则表达式的节点文本组成的列表。

#find()
# 除了find_all()方法，还有find()方法，只不过后者返回的是单个元素，也就是第一个匹配的元素，而前者返回的是所有匹配的元素组成的列表