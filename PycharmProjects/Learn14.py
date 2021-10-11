# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/9/18 2:37 下午
# 文件名称:Learn14.PY
# 开发工具:PyCharm

#关于文件操作IO
import sys

sourcePath = ""
filePath = ""
if len(sys.argv) >= 2:
    listSysParam = sys.argv
    sourcePath = listSysParam[1]
    filePath = sourcePath+"/testFile.txt"

if len(filePath) > 0:
    with open(filePath,"r+") as file: #文件操作使用with语法
        fileContent = file.read()
        print(fileContent)
        print(len(fileContent))
        file.write("winnercrazy\n")
        # file.close()
        pass
print("file over")