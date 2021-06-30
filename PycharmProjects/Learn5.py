# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/6/30 9:54 上午
# 文件名称:Learn5.PY
# 开发工具:PyCharm

#task1
eightNumber = 0o267
valueNumber = int(eightNumber)
twoNumber = 0b10110001
valueNumber = int(twoNumber)
sixNumber = 0xe3a5
valueNumber = int(sixNumber)
print(valueNumber)

#task2
firstStr = "我爱你一生一世"
secondNumber = 520.1314
thirdNumber = 5211314
print("中文：%s 浮点：%f 整数：%d" % (firstStr,secondNumber,thirdNumber))

#task3
array = [73,32,108,111,118,101,32,121,111,117,33]
newArray = []
for tempValue in array:
    newArray.append(chr(tempValue))
task3Str = ''.join(newArray)
print(task3Str)

print('asda'+"321")

