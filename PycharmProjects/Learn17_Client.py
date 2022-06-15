# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 14:42
# 文件名称:Learn17_Client
# 开发工具:PyCharm

'''
Socket
'''

import socket
s = socket.socket()
host = '127.0.0.1'
port = 8080
s.connect((host,port))
send_data = input("输入传送数据:")
s.send(send_data.encode())
recvData = s.recv(1024).decode()
print("接收到的数据:",recvData)
s.close()
