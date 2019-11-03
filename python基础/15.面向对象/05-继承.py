"""---author==hxj---"""
# 1.继承
"""
继承就是让子类直接拥有父类的属性和方法
子类 -- 继承者
父类/超类 -- 被继承者
"""
# 2.怎么继承
"""
1)语法
class 类名(父类1， 父类2....):
    说明文档
    类的内容
2)说明：
() -- 固定写法，如果省略相当于(object)   
    声明类的时候如果没有写父类，默认继承object(object又叫做基类)
    
父类 -- 一个类的父类可以有多个（支持多继承），一般一个
"""


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 声明一个对象方法
    def eat(self, food='noodles'):
        print('{}eat{}'.format(self.name, food))

    # 声明一个类方法
    @classmethod
    def func1(cls):
        print('傻狗')


p1 = Person('abby', 18, 'male')
print(p1.name)


class Student(Person):
    # def __init__(self):
    #     super().__init__()
    # 在子类中添加对象属性,需要先通过super()调用父类的__init__对象属性进行继承后再操作

    def func2(self):
        print('student')
        # 注:super()只能在对象方法和类方法中使用


stu1 = Student()
print(stu1.name)

