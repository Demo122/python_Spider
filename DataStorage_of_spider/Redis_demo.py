#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:18-8-19 下午4:07
"""
#
# edisPy库提供两个类Redis和StrictRedis来实现Redis的命令操作。
#
# StrictRedis实现了绝大部分官方的命令，参数也一一对应，比如set()方法就对应Redis命令的set方法。
# 而Redis是StrictRedis的子类，它的主要功能是用于向后兼容旧版本库里的几个方法。
# 为了做兼容，它将方法做了改写，比如lrem()方法就将value和num参数的位置互换，这和Redis命令行的命令参数不一致。
#
# 官方推荐使用StrictRedis

# ----------------------连接Redis---------------------
# 在本地安装了Redis并运行在6379端口，没有设置密码，密码为None
# from redis import StrictRedis
#
# redis = StrictRedis(host='localhost', port=6379, db=0, password=None)
# redis.set('name','Bob')
# print(redis.get('name')) # b'Bob'

# 我们还可以使用ConnectionPool来连接，示例如下
# from redis import StrictRedis, ConnectionPool
#
# pool = ConnectionPool(host='localhost', port=6379, db=0, password=None)
# redis = StrictRedis(connection_pool=pool)
# 样的连接效果是一样的。观察源码可以发现，StrictRedis内其实就是用host和port等参数又构造了一个ConnectionPool，
# 所以直接将ConnectionPool当作参数传给StrictRedis也一样。

# ConnectionPool还支持通过URL来构建。URL的格式支持有如下3种
# redis://[:password]@host:port/db
# rediss://[:password]@host:port/db
# unix://[:password]@/path/to/socket.sock?db=db
# 这3种URL分别表示创建Redis TCP连接、Redis TCP+SSL连接、Redis UNIX socket连接。
# 我们只需要构造上面任意一种URL即可，其中password部分如果有则可以写，没有则可以省略。下面再用URL连接演示一下：
# from redis import StrictRedis, ConnectionPool
#
# url = 'redis://:@localhost:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
# 首先，声明一个Redis连接字符串，然后调用from_url()方法创建ConnectionPool，接着将其传给StrictRedis即可完成连接
