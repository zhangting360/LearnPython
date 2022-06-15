# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/10 09:18
# 文件名称:Learn17_HomWork
# 开发工具:PyCharm

'''
socket作业
'''

import os

def pingFunction():
    arrSave = []
    for lastAdr in range(1,256):
        lastStr = str(lastAdr)
        cmd = str("ping 192.168.0.%s -c %s -t 1" % (lastStr,"2"))
        result = os.system(cmd)
        if result == 0:
            arrSave.append(lastStr)
    print("有响应的IP = ",arrSave)

if __name__ == "__main__":
    pingFunction()