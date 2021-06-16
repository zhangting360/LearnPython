print("星星之火，可以燎原")

#Task1
print('''
     想要满足用户代码需求
            |
------------------------
| eat our own dog food |
------------------------
''')

print('1''2''3''4')
print('1','3','5')
strArray = ['1','2','3','4']
comversionStr = '!~!'.join(strArray)
print(comversionStr)

import datetime
nowYear = datetime.datetime.now().year
nowMonth = datetime.datetime.now().month
nowHour = datetime.datetime.now().hour
nowMin = datetime.datetime.now().minute
nowSecond = datetime.datetime.now().second
print('Now Year = %s' % nowYear)
print('Now Month = ',nowMonth)
print('Now Hour = ',nowHour)
print('Now Min = ',nowMin)
print('Now Second = ',nowSecond)

nowStr = str(nowYear)
tempStr = 'abc'.join(nowStr)
print(tempStr)

string = "{service}{2}-{0}-{1}".format('1','2','3',service="YOYOService")
print(string)

tempStr = [83,116,97,121]
for value in tempStr:
    str = chr(value)
    print(str,end='')

a = 1
if type(a) == int().__class__ :
    print("相同")
else:
    print("不相同")