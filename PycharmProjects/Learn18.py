# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/10 09:07
# 文件名称:Learn18
# 开发工具:PyCharm

'''
异常处理
'''

import math

def division():
    # math.sqrt(-10)
    num1 = 10
    num2 = 0
    result = num1//num2
    print(result)

if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError:
        print("输入错误:除数不能为0")
    except ValueError as e:
        print("输入错误 ",e);
    else:
        print("执行成功")
    finally:
        print("正确与否都要执行")