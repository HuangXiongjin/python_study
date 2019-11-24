"""---author==hxj---"""
# 1.类中的函数(方法)
"""
1)对象方法
a.怎么声明：直接声明
b.怎么调用：用对象来调用
c.特点：指向当前对象的self
d.什么时候用：如果实现函数的功能需要用到对象属性，就使用对象方法

2)类方法
a.怎么声明：生命在@classmethod
b.怎么调用：用类来调用，"类.类方法名()"
c.特点：自带参数cls；表示当前类，这个参数在调用的时候不用传参数，系统会自动将当前类传给它；
        cls：谁调用就指向谁（如果是对象则指向的是对象对应的类）
d.什么时候用：如果实现函数的功能不需要对象属性，但是需要类的字段，就使用类方法


3)静态方法
a.怎么声明：声明在@staticmethod后面
b.怎么调用：“类.类方法名()”
c.特点：没有默认参数
d.什么时候用：实现函数的功能不需要对象属性，也不需要类的字段
"""


class Person:
    num = 1

    def __init__(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender

    def eat(self, food):
        print("{}在吃{}".format(self.name, food))

    @classmethod
    def func1(cls):  # 类似一个类
        print(cls)

    @staticmethod
    def func2():
        print("静态类", Person.num)


p1 = Person('黄', 18, '男')
Person.func2()
Person.func1()

