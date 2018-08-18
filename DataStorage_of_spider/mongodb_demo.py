#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:18-8-18 下午11:27
"""

# 连接MongoDB
# 连接MongoDB时，我们需要使用PyMongo库里面的MongoClient。
# 一般来说，传入MongoDB的IP及端口即可，其中第一个参数为地址host，第二个参数为端口port（如果不给它传递参数，默认是27017）：
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# 另外，MongoClient的第一个参数host还可以直接传入MongoDB的连接字符串，它以mongodb开头，例如
# client = MongoClient('mongodb://localhost:27017/')
# 这也可以达到同样的连接效果。

# 指定数据库
# MongoDB中可以建立多个数据库，接下来我们需要指定操作哪个数据库。
db = client.test
# # 这里调用client的test属性即可返回test数据库。当然，我们也可以这样指定
# db = client['test']
# 这两种方式是等价的。


# 指定集合
# MongoDB的每个数据库又包含许多集合（collection），它们类似于关系型数据库中的表
# 下一步需要指定要操作的集合，这里指定一个集合名称为students。与指定数据库类似，指定集合也有两种方式

collection = db.students
# collection = db['students']


# 插入数据
# 直接调用collection的insert()方法即可插入数据
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# result = collection.insert(student)
# print(result)  # 5b783e8e3477c52363a3fc8c
# 在MongoDB中，每条数据其实都有一个_id属性来唯一标识。如果没有显式指明该属性，
# MongoDB会自动产生一个ObjectId类型的_id属性。insert()方法会在执行后返回_id值。

# 们也可以同时插入多条数据，只需要以列表形式传递即可
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
# result = collection.insert([student1, student2])
# print(result)
# 返回结果是对应的_id的集合
# [ObjectId('5b783f153477c52410595248'), ObjectId('5b783f153477c52410595249')]

# 在PyMongo 3.x版本中，官方已经不推荐使用insert()方法了。当然，继续使用也没有什么问题。
# 官方推荐使用insert_one()和insert_many()方法来分别插入单条记录和多条记录
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert_one(student)
# print(result)  # <pymongo.results.InsertOneResult object at 0x7ff7bb53f908>
# print(result.inserted_id)  # 5b783f733477c5243af6863e
# # 与insert()方法不同，这次返回的是InsertOneResult对象，我们可以调用其inserted_id属性获取_id

# 对于insert_many()方法，我们可以将数据以列表形式传递
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert_many([student1, student2])
# print(result)  # <pymongo.results.InsertManyResult object at 0x7fc001eec908>
# print(result.inserted_ids)  # [ObjectId('5b783fdb3477c5246d2ee0b2'), ObjectId('5b783fdb3477c5246d2ee0b3')]
# 该方法返回的类型是InsertManyResult，调用inserted_ids属性可以获取插入数据的_id列表

# 查询
