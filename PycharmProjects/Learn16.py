# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/5/18 16:32
# 文件名称:Learn16
# 开发工具:PyCharm

'''
进程和线程
'''

from multiprocessing import Process

def testFunc(interval):
    print('我是子线程')

def main():
    print('主线程开始')
    p = Process(target=testFunc,args =(1,))
    p.start()
    print('主线程结束')

if __name__ == '__main__':
    main()