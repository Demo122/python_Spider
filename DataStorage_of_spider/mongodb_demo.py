#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:18-8-18 下午11:27
"""

# ---------------------------连接MongoDB-------------------------------
# 连接MongoDB时，我们需要使用PyMongo库里面的MongoClient。
# 一般来说，传入MongoDB的IP及端口即可，其中第一个参数为地址host，第二个参数为端口port（如果不给它传递参数，默认是27017）：
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)

# 另外，MongoClient的第一个参数host还可以直接传入MongoDB的连接字符串，它以mongodb开头，例如
# client = MongoClient('mongodb://localhost:27017/')
# 这也可以达到同样的连接效果。

# ----------------------------指定数据库-----------------------------------
# MongoDB中可以建立多个数据库，接下来我们需要指定操作哪个数据库。
db = client.test
# # 这里调用client的test属性即可返回test数据库。当然，我们也可以这样指定
# db = client['test']
# 这两种方式是等价的。


# -----------------------------指定集合-----------------------------------
# MongoDB的每个数据库又包含许多集合（collection），它们类似于关系型数据库中的表
# 下一步需要指定要操作的集合，这里指定一个集合名称为students。与指定数据库类似，指定集合也有两种方式

collection = db.students
# collection = db['students']


# -----------------------------插入数据-----------------------------------
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

# -----------------------------查询-----------------------------------------
# 利用find_one()或find()方法进行查询，其中find_one()查询得到的是单个结果，find()则返回一个生成器对象
# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)
# 这里我们查询name为Mike的数据，它的返回结果是字典类型，运行结果如下：
# <class 'dict'>
# {'_id': ObjectId('5b783f153477c52410595249'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# 它多了_id属性，这就是MongoDB在插入过程中自动添加的

# 我们也可以根据ObjectId来查询，此时需要使用bson库里面的objectid
# from bson.objectid import ObjectId
# result = collection.find_one({'_id': ObjectId('5b783f153477c52410595249')})
# print(result)
# 结果为：{'_id': ObjectId('5b783f153477c52410595249'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# 如果查询结果不存在，则会返回None

# 对于多条数据的查询，我们可以使用find()方法
# results = collection.find({'age': 20})
# print(results)  # <pymongo.cursor.Cursor object at 0x7f0669fd4438>
# for result in results:
#     print(result)
# 返回结果是Cursor类型，它相当于一个生成器，我们需要遍历取到所有的结果，其中每个结果都是字典类型

# 如果要查询年龄大于20的数据，则写法如下：
# results = collection.find({'age': {'$gt': 20}})
# 这里查询的条件键值已经不是单纯的数字了，而是一个字典，其键名为比较符号$gt，意思是大于，键值为20

# 另外，还可以进行正则匹配查询。例如，查询名字以M开头的学生数据，示例如下：
# results = collection.find({'name': {'$regex': '^M.*'}})
# 这里使用$regex来指定正则匹配，^M.*代表以M开头的正则表达式。


# -------------------------------计数----------------------------
# 要统计查询结果有多少条数据，可以调用count()方法。比如，统计所有数据条数
# count=collection.find().count()
# print(count)

# 或者统计符合某个条件的数据：
# count=collection.find({'age':20}).count()
# print(count)

# ------------------------------排序----------------------------
# 排序时，直接调用sort()方法，并在其中传入排序的字段及升降序标志即可。示例如下
# results = collection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results])
# 调用pymongo.ASCENDING指定升序。如果要降序排列，可以传入pymongo.DESCENDING

# ------------------------------偏移---------------------------
# 在某些情况下，我们可能想只取某几个元素，这时可以利用skip()方法偏移几个位置，比如偏移2，就忽略前两个元素，得到第三个及以后的元素：
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])
#
# # 另外，还可以用limit()方法指定要取的结果个数，示例如下：
# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results])
# 如果不使用limit()方法，原本会返回三个结果，加了限制后，会截取前两个结果返回。

# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，因为这样很可能导致内存溢出。
# 此时可以使用类似如下操作来查询
# from bson.objectid import ObjectId
# results=collection.find({'_id': {'$gt': ObjectId('5b783f153477c52410595249')}})
# print([result['name'] for result in results])
# 这时需要记录好上次查询的_id。


# ------------------------------更新----------------------------
# 使用update()方法，指定更新的条件和更新后的数据即可
# condition = {'name': 'Mike'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update(condition, student)
# print(result)
# 这里我们要更新name为Kevin的数据的年龄：首先指定查询条件，然后将数据查询出来，修改年龄后调用update()方法将原条件和修改后的数据传入。
# 运行结果如下:
# {'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
# 返回结果是字典形式，ok代表执行成功，nModified代表影响的数据条数。

# 另外，我们也可以使用$set操作符对数据进行更新，代码如下：
# result = collection.update(condition, {'$set': student})
# 这样可以只更新student字典内存在的字段。如果原先还有其他字段，则不会更新，也不会删除。
# 而如果不用$set的话，则会把之前的数据全部用student字典替换；如果原本存在其他字段，则会被删除。

# 另外，update()方法其实也是官方不推荐使用的方法。这里也分为update_one()方法和update_many()方法，
# 用法更加严格，它们的第二个参数需要使用$类型操作符作为字典的键名
# condition = {'name': 'Mike'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)
# 这里调用了update_one()方法，第二个参数不能再直接传入修改后的字典，而是需要使用{'$set': student}这样的形式，其返回结果是UpdateResult类型。
# 然后分别调用matched_count和modified_count属性，可以获得匹配的数据条数和影响的数据条数。

# 我们再看一个例子：
# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)
# 这里指定查询条件为年龄大于20，然后更新条件为{'$inc': {'age': 1}}，也就是年龄加1，执行之后会将第一条符合条件的数据年龄加1。

# 如果调用update_many()方法，则会将所有符合条件的数据都更新，示例如下：
# condition = {'age': {'$gt': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)
# 这时匹配条数就不再为1条了，运行结果如下：
# <pymongo.results.UpdateResult object at 0x7f598d185788>
# 2 2
# 这时所有匹配到的数据都会被更新。


# ------------------------------删除-------------------------
# 直接调用remove()方法指定删除的条件即可，此时符合条件的所有数据均会被删除
# result = collection.remove({'name': 'Mike'})
# print(result)

# 这里依然存在两个新的推荐方法——delete_one()和delete_many()。示例如下：
# result = collection.delete_one({'name': 'Mike'})
# print(result)
# print(result.deleted_count)
# result = collection.delete_many({'age': {'$lt': 25}})
# print(result.deleted_count)
# delete_one()即删除第一条符合条件的数据，delete_many()即删除所有符合条件的数据。
# 它们的返回结果都是DeleteResult类型，可以调用deleted_count属性获取删除的数据条数。


# --------------------------其他操作----------------------
# 另外，PyMongo还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()和find_one_and_update()
# 它们是查找后删除、替换和更新操作，其用法与上述方法基本一致。

# 另外，还可以对索引进行操作，相关方法有create_index()、create_indexes()和drop_index()等。

