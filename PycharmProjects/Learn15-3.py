# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/5/18 14:11
# 文件名称:Learn15-3
# 开发工具:PyCharm

'''
MySql操作
'''
import pymysql

db = pymysql.connect(host="localhost",user="root",passwd="87923xxx",db=r"TestDataBase")
cur = db.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DataBase Version = %s" % data)
cur.execute("SELECT * From User")
tempData = cur.fetchall()
print('user = ',tempData)
db.close()
