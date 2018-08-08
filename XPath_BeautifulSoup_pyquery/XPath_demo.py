#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/7 22:59
"""

# XPath的常用匹配规则，示例如下：
# //title[@lang='eng']
# 这就是一个XPath规则，它代表选择所有名称为title，同时属性lang的值为eng的节点。

from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
 '''
html = etree.HTML(text)  # 调用HTML类进行初始化，这样就成功构造了一个XPath解析对象
result = etree.tostring(html)  # 调用tostring()方法即可输出修正后的HTML代码，但是结果是bytes类型
print(result.decode('utf-8'))
