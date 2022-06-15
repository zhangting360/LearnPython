# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 16:00
# 文件名称:Learn17_UDP_Server
# 开发工具:PyCharm

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
info = ''
while info != 'by':
    data,addr = s.recvfrom(1024) #在UDP下此方法会阻塞
    info = data.decode()
    print('接受数据 = ',info)
    send_data = input("输入发送数据:")
    s.sendto(send_data.encode(),addr)
s.close()