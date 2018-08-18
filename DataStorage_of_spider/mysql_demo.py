#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/8/15 22:32
"""
import pymysql

# 连接数据库
# db=pymysql.connect(host='localhost',user='root',password='171024',port=3306)
# cursor=db.cursor()
# cursor.execute('SELECT VERSION()')  #execute()方法执行sql语句
# data=cursor.fetchone()    #fetchone()获取查询结果
# print('Database version: ',data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")  #创建spiders数据库，设置默认编码为utf-8
# db.close()


# 创建表
# 创建数据库后，在连接时需要额外指定一个参数db。
# db=pymysql.connect(host='localhost',user='root',password='171024',port=3306,db='spiders')
# cursor=db.cursor()
# sql='CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,age INT NOT NULL,PRIMARY KEY(id))'
# cursor.execute(sql)
# db.close()

# 插入数据
# id = '20120001'
# name = 'Bob'
# age = 20
# db = pymysql.connect(host='localhost', user='root', password='171024', port=3306, db='spiders')
# cursor = db.cursor()
# sql = 'INSERT INTO students(id,name,age) VALUES (%s,%s,%s)'
# try:
#     cursor.execute(sql, (id, name, age))
#     db.commit()
#     #执行玩execute()后要，需要执行db对象的commit()方法才可实现数据插入，这个方法才是真正将语句提交到数据库执行的方法。
#     # 对于数据插入、更新、删除操作，都需要调用该方法才能生效
#     print('ok!')
# except:
#     db.rollback()
#     #我们加了一层异常处理。如果执行失败，则调用rollback()执行数据回滚，相当于什么都没有发生
#     print('not ok!')
# db.close()

# 在很多情况下，我们要达到的效果是插入方法无需改动，做成一个通用方法，只需要传入一个动态变化的字典就好了。
# 然后SQL语句会根据字典动态构造，元组也动态构造，这样才能实现通用的插入方法。所以，这里我们需要改写一下插入方法：
# db = pymysql.connect(host='localhost', user='root', password='171024', port=3306, db='spiders')
# cursor = db.cursor()
# data={
#     'id':'20180818',
#     'name':'mike',
#     'age':22
# }
# table='students'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table,keys=keys,values=values)
# try:
#     if cursor.execute(sql,tuple(data.values())):
#         print('Successful!')
#     db.commit()
# except:
#     print('Failed!')
#     db.rollback()
# db.close()


# 更新数据
db = pymysql.connect(host='localhost', user='root', password='171024', port=3306, db='spiders')
cursor = db.cursor()
# 做简单的数据更新看使用此方法
# sql='UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql,(25,'Bob'))
#     db.commit()
# except:
#     db.rollback()
# db.close()

# 但是在实际的数据抓取过程中，大部分情况下需要插入数据，但是我们关心的是会不会出现重复数据，
# 如果出现了，我们希望更新数据而不是重复保存一次。另外，就像前面所说的动态构造SQL的问题，所以这里可以再实现一种去重的方法，
# 如果数据存在，则更新数据；如果数据不存在，则插入数据。另外，这种做法支持灵活的字典传值
# data = {
#     'id': '20170002',
#     'name': '明红',
#     'age': 20
# }
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
#
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
#                                                                                      values=values)
# update = ','.join(["{key}=%s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successful!')
#         db.commit()
# except:
#     print('Failed!')
#     db.rollback()
# db.close()


# 删除数据
# table = 'students'
# condition = 'age < 20'
#
# sql='DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     if cursor.execute(sql):
#         print('ok')
#     db.commit()
# except:
#     db.rollback()
#
# db.close()


#查询数据
# sql = 'SELECT * FROM students WHERE age >= 20'
#
# try:
#     cursor.execute(sql)
#     print('Count:', cursor.rowcount)
#     one = cursor.fetchone()
#     print('One:', one)
#     results = cursor.fetchall()
#     print('Results:', results)
#     print('Results Type:', type(results))
#     for row in results:
#         print(row)
# except:
#     print('Error')

#调用cursor.rowcount属性获取查询结果的条数
#调用了fetchone()方法，这个方法可以获取结果的第一条数据，返回结果是元组形式
#调用了fetchall()方法，它可以得到结果的所有数据
#但是这里需要注意一个问题，这里显示的是3条数据而不是4条，fetchall()方法不是获取所有数据吗？
# 这是因为它的内部实现有一个偏移指针用来指向查询结果，最开始偏移指针指向第一条数据，取一次之后，指针偏移到下一条数据，
# 这样再取的话，就会取到下一条数据了。我们最初调用了一次fetchone()方法，这样结果的偏移指针就指向下一条数据，
# fetchall()方法返回的是偏移指针指向的数据一直到结束的所有数据，所以该方法获取的结果就只剩3个了。


#我们还可以用while循环加fetchone()方法来获取所有数据，而不是用fetchall()全部一起获取出来。fetchall()会将结果以元组形式全部返回，
# 如果数据量很大，那么占用的开销会非常高。因此，推荐使用如下方法来逐条取数据：
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
