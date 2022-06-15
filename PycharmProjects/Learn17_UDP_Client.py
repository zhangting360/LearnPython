# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 16:02
# 文件名称:Learn17_UDP_Client
# 开发工具:PyCharm

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
response = ""
while response != 'by':
    data = input("输入发送数据:")
    s.sendto(data.encode(),('127.0.0.1',8888))
    response = s.recv(1024).decode()
    print("接收到的数据:",response)
s.close()