#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/15 14:55
"""
import json

# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
# print(type(str))
# data=json.loads(str)
# print(data)
# print(type(data))
#使用loads()方法将字符串转为JSON对象。由于最外层是中括号，所以最终的类型是列表类型。
#果想取第一个元素里的name属性，就可以使用如下方式
# print(data[0]['name'])
# print(data[0].get('name'))  #两者结果一样，推荐使用get()
#这里推荐使用get()方法，这样如果键名不存在，则不会报错，会返回None。另外，get()方法还可以传入第二个参数（即默认值）
# print(data[0].get('age',20))  #在不存在的情况下返回该默认值。

# 值得注意的是，JSON的数据需要用双引号来包围，不能使用单引号。例如，若使用如下形式表示，则会出现错误

#利用dumps()方法，我们可以将JSON对象转为字符串，然后再调用文件的write()方法写入文本
# with open('data.json','w') as f:
#     f.write(json.dumps(data,indent=2))  #参数indent，代表缩进字符个数,使美观

#如果从JSON文本中读取内容，例如这里有一个data.文本文件，其内容是刚才定义的JSON字符串，我们可以先将文本文件内容读出，然后再利用loads()方法转化
# with open('data.json','r') as f:
#     json_str=f.read()
#     data=json.loads(json_str)
#     print(data)



#如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。
# with open('data.json', 'w') as file:
#     json.dump(data,file,indent=2)
#
# with open('data.json','r') as file:
#     data=json.load(file)
#     print(data)


#如果JSON中包含中文字符,写入文件后中文字符都变成了Unicode字符
#为了输出中文，还需要指定参数ensure_ascii为False，另外还要规定文件输出的编码：
data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]
with open('data.json','w',encoding='utf-8') as f:
    f.write(json.dumps(data,indent=2,ensure_ascii=False))