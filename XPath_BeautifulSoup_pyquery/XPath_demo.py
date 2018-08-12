#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/7 22:59
"""

# XPath的常用匹配规则，示例如下：
# //title[@lang='eng']
# 这就是一个XPath规则，它代表选择所有名称为title，同时属性lang的值为eng的节点。


# -----------------------实例--------------------
# from lxml import etree
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
#  '''
# html = etree.HTML(text)  # 调用HTML类进行初始化，这样就成功构造了一个XPath解析对象
# result = etree.tostring(html)  # 调用tostring()方法即可输出修正后的HTML代码，但是结果是bytes类型
# print(result.decode('utf-8'))  # 经过处理之后，li节点标签被补全，并且还自动添加了body、html节点。

# 另外，也可以直接读取文本文件进行解析，示例如下：
# html=etree.parse('./test.html',etree.HTMLParser())
# result=etree.tostring(html)
# print(result.decode('utf-8'))

# --------------------所有节点--------------
# from lxml import etree
#
# html = etree.parse('./test.html', etree.HTMLParser())
# # result=html.xpath('//*')
# # print(result)
# # 这里使用*代表匹配所有节点，也就是整个HTML文本中的所有节点都会被获取
# # 返回形式是一个列表，每个元素是Element类型，其后跟了节点的名称，如html、body、div、ul、li、a等，所有节点都包含在列表中了
#
# # 此处匹配也可以指定节点名称。如果想获取所有li节点
# result = html.xpath('//li')
# print(result)
# print(result[0])
# # 这里可以看到提取结果是一个列表形式，其中每个元素都是一个 Element对象。如果要取出其中一个对象，可以直接用中括号加索引，如[0]


# ------------------子节点---------------------
# 我们通过/或//即可查找元素的子节点或子孙节点。假如现在想选择li节点的所有直接a子节点，可以这样实
# from lxml import etree
#
# html = etree.parse('./test.html', etree.HTMLParser())
# # result=html.xpath('//li/a')
# # 这里通过追加/a即选择了所有li节点的所有直接a子节点。因为//li用于选中所有li节点，
# # /a用于选中li节点的所有直接子节点a，二者组合在一起即获取所有li节点的所有直接a子节点。
#
# # 如果要获取所有子孙节点，就可以使用//。例如，要获取ul节点下的所有子孙a节点，可以这样实现：
# result = html.xpath('//ul//a')
# # 但是如果这里用//ul/a，就无法获取任何结果了。因为/用于获取直接子节点，而在ul节点下没有直接的a子节点，只有li节点，所以无法获取任何匹配结果，
# print(result)
# # 因此，这里我们要注意/和//的区别，其中/用于获取直接子节点，//用于获取子孙节点


# ------------------父节点----------------------
# 们知道通过连续的/或//可以查找子节点或子孙节点，那么假如我们知道了子节点，怎样来查找父节点呢？这可以用..来实现。
# 比如，现在首先选中href属性为link4.html的a节点，然后再获取其父节点，然后再获取其class属性，相关代码如下：
# from lxml import etree
#
# html=etree.parse('./test.html',etree.HTMLParser())
# # result=html.xpath('//a[@href="link4.html"]/../@class')
# #同时，我们也可以通过parent::来获取父节点，代码如下：
# result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)


# ------------------属性匹配----------------
# 在选取的时候，我们还可以用@符号进行属性过滤。比如，这里如果要选取class为item-1的li节点，可以这样实现:
# from lxml import etree
# html=etree.parse('./test.html',etree.HTMLParser())
# result=html.xpath('//li[@class="item-1"]')
# print(result)


# ------------------文本获取-----------------
# 们用XPath中的text()方法获取节点中的文本，接下来尝试获取前面li节点中的文本
# from lxml import etree
#
# html = etree.parse('./test.html', etree.HTMLParser())
# # result=html.xpath('//li[@class="item-0"]/text()')
# # 运行结果为['\n     ']
# # 因为XPath中text()前面是/，而此处/的含义是选取直接子节点，很明显li的直接子节点都是a节点，文本都是在a节点内部的，
# # 所以这里匹配到的结果就是被修正的li节点内部的换行符，因为自动修正的li节点的尾标签换行了
#
# # 果想获取li节点内部的文本，就有两种方式，一种是先选取a节点再获取文本，另一种就是使用//
# # result=html.xpath('//li[@class="item-0"]/a/text()') #['first item', 'fifth item']
# result = html.xpath('//li[@class="item-0"]//text()')  # ['first item', 'fifth item', '\n    ']
# print(result)
# # 果要想获取子孙节点内部的所有文本，可以直接用//加text()的方式，这样可以保证获取到最全面的文本信息，
# # 但是可能会夹杂一些换行符等特殊字符。如果想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，
# # 然后再调用text()方法获取其内部文本，这样可以保证获取的结果是整洁的。


# ---------------------属性获取-------------------
# 我们知道用text()可以获取节点内部文本，那么节点属性该怎样获取呢？其实还是用@符号就可以。
# 例如，我们想获取所有li节点下所有a节点的href属性，代码如下：
# from lxml import etree
#
# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li/a/@href')
# # 注意，此处和属性匹配的方法不同，属性匹配是中括号加属性名和值来限定某个属性，
# # 如[@href="link1.html"]，而此处的@href指的是获取节点的某个属性，二者需要做好区分。
# print(result)


# --------------------属性多值匹配---------------------
# #有时候，某些节点的某个属性可能有多个值，例如：
# from lxml import etree
#
# text = '''
# <li class="li li-first"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# # 这里HTML文本中li节点的class属性有两个值li和li-first，此时如果还想用之前的属性匹配获取，就无法匹配了
# # result = html.xpath('//li[@class="li"]/a/text()')  # []
# # 这时就需要用contains()函数了，代码可以改写如下：
# result = html.xpath('//li[contains(@class,"li")]/a/text()')  # ['first item']
# # 通过contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所传入的属性值，就可以完成匹配了
# print(result)


# --------------------多属性匹配-------------------------
# 我们可能还遇到一种情况，那就是根据多个属性确定一个节点，这时就需要同时匹配多个属性。此时可以使用运算符and来连接，示例如下
# from lxml import etree
#
# text = '''
# <li class="li li-first" name="item"><a href="link.html">first item</a></li>
# '''
# html = etree.HTML(text)
# result = html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
# print(result)  # ['first item']
# # 要确定这个节点，需要同时根据class和name属性来选择，一个条件是class属性里面包含li字符串，另一个条件是name属性为item字符串，
# # 二者需要同时满足，需要用and操作符相连，相连之后置于中括号内进行条件筛选。
# # 这里的and其实是XPath中的运算符


# --------------------按序选择-----------------------
# 时候，我们在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，如第二个节点或者最后一个节点，这时该怎么办呢？
# 这时可以利用中括号传入索引的方法获取特定次序的节点，示例如下：
# from lxml import etree
# text='''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html=etree.HTML(text)
# # html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[1]/a/text()')
# print(result)
# result = html.xpath('//li[last()]/a/text()')
# print(result)
# result = html.xpath('//li[position()<3]/a/text()')
# print(result)
# result = html.xpath('//li[last()-2]/a/text()')
# print(result)
# 第一次选择时，我们选取了第一个li节点，中括号中传入数字1即可。注意，这里和代码中不同，序号是以1开头的，不是以0开头。
# 第二次选择时，我们选取了最后一个li节点，中括号中传入last()即可，返回的便是最后一个li节点。
# 第三次选择时，我们选取了位置小于3的li节点，也就是位置序号为1和2的节点，得到的结果就是前两个li节点。
# 第四次选择时，我们选取了倒数第三个li节点，中括号中传入last()-2即可。因为last()是最后一个，所以last()-2就是倒数第三个。
# 输出结果
# ['first item']
# ['fifth item']
# ['first item', 'second item']
# ['third item']


# --------------------节点轴选择-----------------------------
# XPath提供了很多节点轴选择方法，包括获取子元素、兄弟元素、父元素、祖先元素等，示例如下：
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)

# 第一次选择时，我们调用了ancestor轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器，
# 这里我们直接使用*，表示匹配所有节点，因此返回结果是第一个li节点的所有祖先节点，包括html、body、div和ul。
result = html.xpath('//li[1]/ancestor::*')
print(result)

# 弟二次选择时，我们又加了限定条件，这次在冒号后面加了div，这样得到的结果就只有div这个祖先节点了。
result = html.xpath('//li[1]/ancestor::div')
print(result)

# 第三次选择时，我们调用了attribute轴，可以获取所有属性值，其后跟的选择器还是*，这代表获取节点的所有属性，
# 返回值就是li节点的所有属性值。
result = html.xpath('//li[1]/attribute::*')
print(result)

# 第四次选择时，我们调用了child轴，可以获取所有直接子节点。这里我们又加了限定条件，选取href属性为link1.html的a节点。
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)

# 五次选择时，我们调用了descendant轴，可以获取所有子孙节点。这里我们又加了限定条件获取span节点，
# 所以返回的结果只包含span节点而不包含a节点。
result = html.xpath('//li[1]/descendant::span')
print(result)

# 第六次选择时，我们调用了following轴，可以获取当前节点之后的所有节点。（不包括挡墙节点的子孙节点，从同级节点开始）
# 这里我们虽然使用的是*匹配，但又加了索引选择，所以只获取了第二个后续节点。
result = html.xpath('//li[1]/following::*[2]')
print(result)

# 第七次选择时，我们调用了following-sibling轴，可以获取当前节点之后的所有同级节点。这里我们使用*匹配，所以获取了所有后续同级节点。
result = html.xpath('//li[1]/following-sibling::*')
print(result)

# 以上是XPath轴的简单用法，更多轴的用法可以参考：http://www.w3school.com.cn/xpath/xpath_axes.asp。
