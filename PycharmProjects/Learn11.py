# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/7/26 4:01 下午
# 文件名称:Learn11.PY
# 开发工具:PyCharm

#函数
def function1():
    ...
    print("hello world")
def function2():
    pass
    print("function1")
function1()
function2()

def function3(myList):
    for value in myList:
        print("value  = ",value)
function3((1,2,3,4,"哟西"))

def function4(number):
    return number*number
tmpNumber = function4(4)
print("number = ",tmpNumber)

#global 声明调用全局变量
myProperty = 100
def function5():
    global myProperty
    myProperty = 1010
    print(myProperty)
function5()
print(myProperty)

#匿名函数 -- lambda
import math
r = 100
result = lambda r:math.pi*r*r #获取圆面积
print("半径 =",r,"圆的面积 =",result(r))

#HomeWork
def conversionToString(valueString):
    if type(valueString) == str:
        tempList = []
        for tempChar in valueString:
            if tempChar == "0":
                tempList.append("O")
            elif tempChar == "3":
                tempList.append("E")
            elif tempChar == "1":
                tempList.append("L")
            else:
                tempList.append(tempChar)
        finishString = "".join(tempList)
        return finishString
    else:
        return ""
successStr = conversionToString("12302")
print(successStr)

# 1人民币 = 9.912卢布
def moneyConversionToRussion(moneyNumber):
    finishNum = moneyNumber * 9.912
    return finishNum
number = moneyConversionToRussion(1200)
print(number)

RMBtoRussion = lambda mon:mon * 9.912
successNumber = RMBtoRussion(1200)
print(successNumber)
