# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 15:01
# 文件名称:Server
# 开发工具:PyCharm

'''
关于socket套接字
'''
import os
import socket

#打印进程ID
pid = os.getpid()
print("进程ID = ",pid)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
s.bind((host,port))
s.listen(1)
print('等待消息接收')
sock,addr = s.accept()
print('接受到消息')
response = sock.recv(1024).decode()
while response != 'byby':
    if response:
        print("接收到的内容:",response)
    send_data = input("请输入返回的内容:")
    sock.send(send_data.encode())
    if send_data == 'byby':
        break
    response = sock.recv(1024).decode()
sock.close()
s.close()