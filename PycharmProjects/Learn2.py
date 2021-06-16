# 开发人员:zhangting
# 开始时间:2021/5/12 12:40 下午
# 文件名称:Learn2.PY
# 开发工具:PyCharm

print(r'哈哈哈\nYOYO')

a = int('10110001',2)
if a == 177:
    print("OK")
else:
    print('NO')

array = [73,32,108,111,118,101,32,121,111,117,33]
for value in array:
    a = chr(value)
    print(a,end="")

a = 3%5
print(a)

a = ['111','222','333']
b = ''.join(a)
print(b)

array = []
inputString1 = input("第一次请输入:")
inputString2 = input("第二次请输入:")
inputString3 = input("第三次请输入:")
array.append(inputString1)
array.append(inputString2)
array.append(inputString3)
asd = 0
for tempValue in array:
    valueInt = int(tempValue)
    asd+=valueInt
print('asd = ',asd)

a = enumerate(array)
print(a)
for index,value in a:
    print(index,value)

print("个数 = ",len(array))
