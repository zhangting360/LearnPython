# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/7/19 5:18 下午
# 文件名称:Learn10.PY
# 开发工具:PyCharm

import random
#字典
dic1Obj = dict(你好="阿萨德",世界="中国",国外="美国")
dic2Obj = {'qq':"抄袭","number":1234,"asd":12.3}
dic3Obj = {(123,321):"测试元组Key",4:"Number Four"}
print(dic1Obj)
print(dic2Obj)
print(dic3Obj)
for value in dic2Obj.values():
    print("value = ",value)
    # print("key = ",key,"value = ",value)

for value in dic3Obj:
    print(value)

#zip函数
list1 = ["1",'2','3']
list2 = ["张","李","刘"]
zippoObj = zip(list1,list2)
zippoTulpe = dict(zippoObj)
# listFinished = dict(zippoObj)  #注意:zip函数返回可迭代类型，如果执行此句，后面不会print出任何东西
# print("zippo = ",zippoObj)
for value in zippoObj:
    print("value = ",value)
print('zippoDic = ',zippoTulpe)

# dicObj1 = dict(1 = 123,2 = "Japan")  #注意:必须符合赋值语句的规则，数字是不能作为变量名的
# print(dicObj1)

list1 = [1,2,3,4,5,6]
dictionary = dict.fromkeys(list1)
print('dic = ',dictionary)
tmp1 = zippoTulpe.pop('1')
print(tmp1)
tmp2 = zippoTulpe.popitem()
print("tmp2 = ",tmp2)
print(zippoTulpe)

dic1 = {"First":"China","Second":"America","Third":"Canada"}
print(dic1.get("1","没有"))
value = "First"
if dic1.get(value):
    print(dic1.get(value))
else:
    print("没有")
for item in dic1.items():
    print("item = ",item)
for (key,value) in dic1.items():
    print("key = %s, value = %s" % (key,value))
for key in dic1.keys():
    print("key = ",key)
for value in dic1.values():
    print("value = ",value)
dic1.pop("First")
print("dic1 = ",dic1)

randomDic = {i:random.randint(10,10000) for i in range(1,5)} #字典推导式
print('randomDic = ',randomDic)

#集合 -- 不重复元素
setObj = {1,2,4,5,6,8,1,2,4,5,7,6,8}
print(setObj)
listSet = ["A",'B','C','D',"A","D"]
set1 = set(listSet)
print(set1)
tempStr = "极限挑战"
strSet = set(tempStr)
print("StrSet = ",strSet)