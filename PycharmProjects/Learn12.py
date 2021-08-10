# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2021/8/10 3:10 下午
# 文件名称:Learn12.PY
# 开发工具:PyCharm

class Animal:
    tiger = "东北虎"
    fish = "鲨鱼"
    bird = "老鹰"
    def __init__(self,firstName,secondName,thirdName):
        print("I'm Animal")
        print(firstName)
        print(secondName)
        print(thirdName)
tmp1Animal = Animal("老虎","狮子","海豚")
tmp2Animal = Animal("YOYO","HOHO","HAHA")
print(tmp1Animal.tiger)
tmp2Animal.tiger = "非洲狮子"
print(tmp2Animal.tiger)
Animal.tiger = "小狮子"
print(Animal.tiger)