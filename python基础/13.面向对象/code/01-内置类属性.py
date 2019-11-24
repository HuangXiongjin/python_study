"""---author==hxj---"""
# 1.什么是内置类属性
"""
声明类的时候系统自动添加的属性（可能是字段属性也可能是对象属性）
"""


class Person:
    """
    name: 人的名字
    gender: 人的性别
    age: 人的年龄
    """

    num = 10

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self, food):
        print("{}在吃{}".format(self.name, food))

    def __str__(self):
        print(self)


p1 = Person('小黄黄', '男', 20)
p1.eat('冰粉')

# 1.__name__
"""
类的字段；类.__name__ ---获取类的名字（字符串）
"""
print(Person)
print(Person.__name__)

# 2.__doc__
"""
类的字段；类.__doc__ ---获取类的说明文档
"""
print(Person.__doc__)
print(int.__doc__)
print("==============================================")
# 3.__class__
"""
对象的属性；对象.__class__ -- 获取对象对应的类，返回的是类（和type（对象）功能一样）
"""
print(p1.__class__)


# 4.__dict__  (将对象转换成字典)
"""
对象属性；对象.__dict__ -- 将对象所有的属性和对应的值转换成一个字典中的键值对（一个对象对应一个字典）
类的字段；类.__dict__ -- 将类转换成一个字典，字典中的元素是类中所有的字段和对应的值
"""
print(p1.__dict__)
print(Person.__dict__)  # 声明函数就是声明变量，变量也属于字段


# print(p1)


# 5.__module__
"""
类的字段；类.__module__ --- 获取当前类是哪个模块中声明的（返回的是模块的名字）
"""
print(Person.__module__)  # __main__
print(bool.__module__)  # builtins

# 6.__bases__
"""
类的字段；类.__bases__ -- 获取当前类的父类（返回的是一个元组）
"""
print(Person.__bases__)


