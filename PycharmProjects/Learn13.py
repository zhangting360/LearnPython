# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/8/10 5:21 下午
# 文件名称:Learn13.PY
# 开发工具:PyCharm

#模块
import ModuleTest
import ModuleTest as modeTest #导入模块并用modeTest代替别名
ModuleTest.getInfo()
# from ModuleTest import getInfo #导入模块的getInfo函数
from ModuleTest import * #导入模块所有（类，函数...）
getInfo()
print("Dir = ",dir())

import sys
systemPathList = sys.path
for sysPath in systemPathList:
    print(sysPath)

import time

print(time.time()) #当前时间戳
timeData = time.localtime(time.time())
print("时间数据 = ",timeData)
print("%s年%s月%s日 %s时%s分%s秒" % (timeData.tm_year,timeData.tm_mon,timeData.tm_mday,timeData.tm_hour,timeData.tm_min,timeData.tm_sec))

import calendar
cal = calendar.month(2021,1)
print(cal)