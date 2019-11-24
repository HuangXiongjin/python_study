"""---author==hxj---"""
# 1.多继承
"""
python中的类支持多继承，也就是让一个类有多个父类。
"""


class Animal(object):
    num = 100

    def __init__(self):
        self.age = 0
        self.gender = '雌'

    @classmethod
    def func2(cls):
        print('动物类的类方法。')


class Fly(object):
    name = '飞'

    def __init__(self):
        self.height = 100
        self.time = 5
        self.speed = 100

    def func2(self):
        print('飞行的对象的方法。')


class Bird(Animal, Fly):
    pass


bird1 = Bird()
print(Bird().num, Bird().name)
print(Bird.num, Bird.name)
print(bird1.num, bird1.name)

print(bird1.gender)
"""
多继承的时候，在继承属性的时候，只继承了第一个父类(Animal)的所有的属性，在子类调用到第二个父类中的属性的时候则会
出现AttributeError 错误
"""
# print(bird1.speed)   # AttributeError: 'Bird' object has no attribute 'speed'

