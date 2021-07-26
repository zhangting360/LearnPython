# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/7/6 3:47 下午
# 文件名称:Learn7.PY
# 开发工具:PyCharm

#字符串
string = "@收到货富士康.@."
print(string.strip('@.收康士'))
firstStr = string[0:2]
lastStr = string[len(string)-3:len(string)]
print(firstStr)
print(lastStr)