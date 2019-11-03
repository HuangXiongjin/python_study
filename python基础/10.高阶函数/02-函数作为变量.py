"""---author==hxj---"""
# 1.python中声明函数就是声明类型是function的变量，函数名就是变量名
"""
普通变量能做的事情，函数都可以做
"""
# 1)




# 2)修改变量的值


# 3)变量作为序列的元素
# def func1():
#
#
# func1()
#
#
# list2 = [func1, func1(), 10]
# print(list2)

# 4)作为函数的参数
def func2(x):
    print(x)

a = 10
func2(a)


# 5)变量作为函数的返回值
def func3(x, y):
    num = x + y
    return num


print(func3(1, 4))


def func4():
    def func5():
        print('函数5')
    return func5()


# print(func4())
func4()()
