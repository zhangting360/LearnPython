# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/8 13:04
# 文件名称:Learn17
# 开发工具:PyCharm

'''
socket套接字
'''

import socket

host = '127.0.0.1'
port = 8080
webSocket = socket.socket()
webSocket.bind((host,port))
webSocket.listen(5)
print('服务器等待客户端连接...')
while True:
    print("while循环开始")
    con,addr = webSocket.accept() #此方法阻塞等待client消息，不会向下运行
    data = con.recv(1024).decode()
    print('接收到的数据 = ',data)
    con.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello Fuck')
    con.close()
    print("while循环结束")