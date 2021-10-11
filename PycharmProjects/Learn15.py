# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/10/11 4:57 下午
# 文件名称:Learn15.PY
# 开发工具:PyCharm

#数据库操作
import sqlite3

#创建数据库，如没有自动创建
conn = sqlite3.connect('microsoft.db')
#游标
cursor = conn.cursor()
#数据库语句，创建数据
cursor.execute('create table user (id int(10) primary key, name varchar(20))')
cursor.close()
conn.close()

