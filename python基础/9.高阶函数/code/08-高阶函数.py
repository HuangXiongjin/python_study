"""---author==hxj---"""
# 装饰器 = 实参高阶函数 + 返回值高阶函数 + 糖用法
# 1.实参高阶函数
"""
参数是函数 的函数就是 实参高阶函数。
python中内置的sorted, max, min等函数，以及列表的sort方法都是实参高阶函数。
这些函数中都有一个参数key,要求传参的时候传一个函数。
这个函数需要一个参数和一个返回值，参数代表序列中的元素，返回值才是比较对象
"""


def hi():
    return "hi yasoob!"


# func = hi
# print(func())
def doSomethingBeforeHi(func):  # func = hi
    print("I am doing some boring work before executing hi()")
    print(func())  # 相当于print(hi())


doSomethingBeforeHi(hi)


# num = [1, 76, 89, 90]
#
# def func1(num):
#     return num % 10
#
#
# num.sort(key=func1)
# print(num)
#
# # 按照字典中的key为'score'的值从小到大排序
# dicts = [
#     {'name': '小明1', 'score': 98},
#     {'name': '小明2', 'score': 34},
#     {'name': '小明3', 'score': 56},
#     {'name': '小明4', 'score': 77},
#     {'name': '小明5', 'score': 89},
# ]
# def func2():
#     return dicts['score']
#
# dicts.sort(key=func2, dicts: dicts['score'])
# print(dicts)
#

