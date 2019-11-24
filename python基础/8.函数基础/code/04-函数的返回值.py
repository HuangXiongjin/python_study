"""---author---hxj""""

# 1. 什么是返回值
"""
返回值就是return关键字后表达式的值 (怎么确定函数的返回值)
返回值就是函数调用表达式的值 (怎么获取函数的返回值)
(python中所有函数都有返回值，默认是None)

1)什么是return
return是函数体中的关键字(只能在函数中使用), 作用有两个: 结束函数\确定函数返回值
a.结束函数: 执行函数体的时候只要遇到return函数直接结束
b.确定函数返回值: return 返回值(可以是具体的数据，声明过的变量，运算表达式)

2)什么是函数调用表达式
函数调用语句就是函数调用表达式, 例如: func1(10), max([1, 2]),
每个调用函数的语句都有结果，这个结果就是调用这个函数得到的返回值
"""


def func1():
    for x in range(10):
        if x == 2:
            return
        print(x)
    print('里面: 函数结束')


print('func1:', func1())


def func2():
    print('=====')
    return
    print('++++++')
    print('------')


print('func2:', func2())


def func3():
    if False:
        return 10

print('func3:', func3())


def func4():
    return 100

print('func4:', func4())

# 2.怎么使用返回值
"""
想要用函数的返回值，就使用函数调用表达式的值。
普通数据能做的事情，函数调用表达式都可以做
"""
100
func4()

num = 100
num1 = func4()
print(num, num1)

list1 = [100, 200]
list2 = [func4(), 200]
print(list1, list2)

print(100 > 200, 100 * 2)
print(func4() > 200, func4()*2)


# 3.什么时候需要返回值
"""
初学者：看实现函数的功能会不会产生新的数据
return 返回值1,返回值2,...
"""


def sum1(num1, num2):
    return num1 + num2


re = sum1(10, 20)
print(re)
list1 = [re, 20]


