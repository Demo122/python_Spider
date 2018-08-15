#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/15 15:54
"""

#1.写入
import csv

#调用csv库的writer()方法初始化写入对象，传入该句柄，然后调用writerow()方法传入每行的数据即可完成写入
# with open('data.csv','w') as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','mike',20])
#     writer.writerow(['10002','july',21])
#     writer.writerow(['10003','lisa',23])


#如果想修改列与列之间的分隔符，可以传入delimiter参数
# with open('data.csv','w') as csvfile:
#     writer=csv.writer(csvfile,delimiter=' ')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','mike',20])
#     writer.writerow(['10002','july',21])
#     writer.writerow(['10003','lisa',23])


#可以调用writerows()方法同时写入多行，此时参数就需要为二维列表
# with open('data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])


#但是一般情况下，爬虫爬取的都是结构化数据，我们一般会用字典来表示。在csv库中也提供了字典的写入方式
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
#这里先定义3个字段，用fieldnames表示，然后将其传给DictWriter来初始化一个字典写入对象，接着可以调用writeheader()方法先写入头信息，
# 然后再调用writerow()方法传入相应字典即可。最终写入的结果是完全相同的

#如果要写入中文内容的话，可能会遇到字符编码的问题，此时需要给open()参数指定编码格式
#比如，这里再写入一行包含中文的数据，代码需要改写如下
# with open('data.csv', 'a', encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})

#如果接触过pandas等库的话，可以调用DataFrame对象的to_csv()方法来将数据写入CSV文件中。

#2. 读取
#这里我们构造的是Reader对象，通过遍历输出了每行的内容，每一行都是一个列表形式。注意，如果CSV文件中包含中文的话，还需要指定文件编码。
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


#如果接触过pandas的话，可以利用read_csv()方法将数据从CSV中读取出来，
# import pandas
#
# data=pandas.read_csv('data.csv')
# print(data)
#在做数据分析的时候，此种方法用得比较多，也是一种比较方便地读取CSV文件的方法。