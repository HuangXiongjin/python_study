"""---author==hxj---"""
# 1.什么是回调函数：函数的调用是在其他函数的内部满足条件的时候自动调用的函数
# 在计算机程序设计中，回调函数简称回调（callback），指的是通过函数参数传递到其他代码的，某一块可用执行代码的应用。


def my_callback(input):
    print("function my_callback was called with %s input" % input)


def caller(input, func):
    func(input)


for i in range(5):
    caller(i, my_callback)
