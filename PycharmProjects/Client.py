# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 15:47
# 文件名称:Client
# 开发工具:PyCharm

'''
Socket套接字
'''

import socket
import os

#打印进程ID
pid = os.getpid()
print("进程ID = ",pid)

s = socket.socket()
host = '127.0.0.1'
port = 12345
s.connect((host,port))
print('已连接')
info = ""
while info != 'byby':
    send_data = input("输入想发送的内容:")
    s.send(send_data.encode())
    if send_data == 'byby':
        break
    info = s.recv(1024).decode()
    print("接受的内容",info)
s.close()