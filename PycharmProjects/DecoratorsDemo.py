#闭包函数,装饰器
#闭包:参数为函数，返回为函数，为了增强函数
#装饰器:类似;本质为函数闭包

def functionFather(func):
    def dealFunction():
        print('I`m functionFather Start')
        func()
        print('I`m functionFather End')
    return dealFunction

@functionFather
def kidsFunction():
    print("I'm Kids")

if __name__ == "__main__":
    # function = functionFather(kidsFunction)
    kidsFunction()
