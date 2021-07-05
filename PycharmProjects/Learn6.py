# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/6/30 3:49 下午
# 文件名称:Learn6.PY
# 开发工具:PyCharm

'''
关于"列表和元组"
序列:列表，元组，字典，字符串，集合
'''

#倒数计数
array = ["美国","中国","法国","英国","德国","日本","韩国","澳大利亚","加拿大","俄罗斯"]
print(array[-1])
print(array[3])

#切片
print(array[0:100:4])

#复制值
tempArray = array[:]
array.append("意大利")
print(array,tempArray)

#序列相加
array1 = ["Java","C","Python","Object","Swift"]
array2 = ["Xcode","VSCode","Linux","Web"]
arrayResult = array1+array2
print(arrayResult)

#相乘
arrayMul = arrayResult*5
print(arrayMul)

#是否包含
isContain = "Python" in array1
if isContain:
    print("存在")
else:
    print("不存在")
isContain = "C" not in array2
if isContain:
    print("不存在")
else:
    print("存在")

#计算长度，最大值，最小值
num = [11,2,88,76,119,27,932]
print("长度 = ",len(num))
print("最大值 = ",max(num))
print("最小值 = ",min(num))

numStr = ["你","我","他"]
print("长度 = ",len(numStr))
print("最大值 = ",max(numStr))
print("最小值 = ",min(numStr))

tempStr = "China Number1"
arrayStr = list(tempStr)
print(arrayStr)

arrayStr = str(tempStr)
print(arrayStr)
print(sum(num))

#列表
array = list(range(0,100))
print(array)
array = list(range(100,120,2))
print(array)
del array #删除列表

a = object()
b = object()
objects = [a,b,a,a,a]
aCount = objects.count(a)
print("count = ",aCount)
print("index = ",objects.index(b))

numbers = [11,2,53,41,52,16,27,78,189,110]
sumTotal = sum(numbers)
print(sumTotal)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

chars = ["world","hello","wow","Tom","Orrange","China"]
chars.sort()
print(chars)
chars.sort(key=str.lower)
print(chars)

#列表推导式
aaaa = []
resultArray = [[aaaa.append(str(value)+"*"+str(value2)+"="+str(value*value2)) for value2 in range(value,10)] for value in range(1,10)]
print("result = ",resultArray)
for tempValue in resultArray:
    print(tempValue)
print('aaaa = ',aaaa)

#元组
