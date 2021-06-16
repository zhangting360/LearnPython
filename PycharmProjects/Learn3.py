# 开发人员:zhangting
# 开始时间:2021/5/14 4:06 下午
# 文件名称:learn3.PY
# 开发工具:PyCharm

rangeObject = range(0,100,2)
listRange = list(rangeObject)
enum = enumerate(rangeObject)
for value in enum:
    print('value = ',value)
print(rangeObject)

lenArray =  len(listRange)
countArray = listRange.count(1)
print('len = ',lenArray,'count = ',countArray)

import random

array = []
randomNumber = [random.randint(10,100) for i in range(10)]
randomObject = random.randint(10,100)
print('随机数 = ',randomNumber)
print('random object = ',randomObject)

i = 0
while i < 10:
    print(random.randint(200,300))
    i+=1

#HomeWork
array = [89,98,00,75,68,37,58,90]
tempArray = []
for value in array:
    result = value+1900
    tempArray.append(result)
print('tempArray = ',tempArray)

array.sort(reverse=True)
print('array =',array)