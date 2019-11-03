"""---author==hxj---"""
# 1.构造函数 --- 函数名和类名一样，用来创建类的对象的函数
"""
python中声明类的时候，系统会自动为这个类创建一个构造函数，函数的作用就是创建对象。
构造方法的执行过程：
a.在内存中开辟空间创建对象
b.用创建好的对象去调用__init__方法
c.返回对像在内存中的地址
"""
# 2.__init__方法
"""
声明在类中用来对对象进行初始化的方法（当对象一创建出来，这个方法就会被自动调用）

注意：创建对象的时候构造方法需不需要传参数，需要几个参数，看这个类的__init__方法需要传几个参数
"""


# class Dog:
#     def __init__(self, name, age):
#         print("调用")
#         print(name, age)


# Dog()  # 类名后面加上()那么这个对象就被创建，会调用类里面的方法
# dog1 = Dog()  # 当对象一创建出来，这个方法就会被自动调用
# dog1 = Dog('df', 0)

#
"""

"""


# def __init__(a, b):
#     print("a", a)
#     print("a", b)
#
#
# def Dog(a, b):
#     __init__(a, b)
#
#
# Dog(10, 23)
def __init__(a, b):
    print("a")
    print("a")


def Dog(*args, **kwargs):
    __init__(*args, **kwargs)


Dog(10, 23)

