# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/10/11 4:57 下午
# 文件名称:Learn15.PY
# 开发工具:PyCharm

#数据库操作
import sqlite3

#创建数据库，如没有自动创建
# conn = sqlite3.connect('microsoft.db')
#游标
# cursor = conn.cursor()
#数据库语句，创建表单
"""
cursor.execute('create table user (id int(10) primary key, name varchar(20))')
cursor.close()
conn.close()
"""
"""
db = sqlite3.connect('microsoft.db')
cursor1 = db.cursor()
#创建数据
cursor1.execute('insert into user(id,name) values ("1", "ZhangTing")')
cursor1.execute('insert into user(id,name) values ("2", "ZhangSan")')
cursor1.execute('insert into user(id,name) values ("3", "ZhangJin")')
#查询数据
cursor1.execute('select * from user')
result = cursor1.fetchall()
print(result)
#创建表
# cursor1.execute('create table Person (id int(10) primary key, name varchar(20), age int(10), Flag varchar(20))')
#该表中创建数据
cursor1.execute('insert into Person(id,name,age,Flag) values ("1","Joy", "21", "Happy")')
cursor1.execute('insert into Person(id,name,age,Flag) values ("2","Tony", "32", "Bad")')
cursor1.execute('insert into Person(id,name,age,Flag) values ("3","Ella", "16", "School")')
#读取数据
cursor1.execute('select * from Person')
result = cursor1.fetchall()
print('Person数据 = ',result)
#提交所执行的事务
db.commit()
#关闭
cursor1.close()
db.close()
"""
#更新和删除操作
updateDB = sqlite3.connect('microsoft.db')
cursor2 = updateDB.cursor()
cursor2.execute('update Person set name = ? where id = ?',('ZhangSir',3))
cursor2.execute('delete from Person where id = ?',(1,))
updateDB.commit()
cursor2.close()
updateDB.close()

