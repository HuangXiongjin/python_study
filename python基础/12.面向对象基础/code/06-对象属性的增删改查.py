"""---author==hxj---"""


# python中类的对象属性支持增删改查
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person('小明', 18, '男')
p2 = Person('小红', 20, '女')

# 1.查（获取属性的值）
"""
方法1：对象.属性
方法2：getattr(对象，属性名:str)  # attribute -- 属性
方法3：对象.__getattribute__(属性名)
"""
print(p1.name)
print(getattr(p1, 'name'))
print(getattr(p1, 'age'))
print(p1.__getattribute__('gender'))
# value = input('属性名：')
# print(getattr(p1, value))
# value = input('属性名：')
# print(p1.__getattribute__(value))

# 2.增和改
"""
方法1：对象.属性 = 值
方法2: 
"""

# 属性不存在就添加
p1.weight = 190
print(p1.weight)

# 3.删
"""
方法1：del 对象.属性
方法2：delattr(对象，属性名)
"""
del p1.name
# print(p1.name)  # AttributeError: 'Person' object has no attribute 'name'

delattr(p1, 'age')


# print(p1.age)  # AttributeError: 'Person' object has no attribute 'age'

# 4.__slots__魔法
# 通过给__slots__字段赋值来约束当前类的对象有哪些对象属性


class Dog:
    __slots__ = ('name', 'age')  # 使用__slots__魔法以后，在外面就只能使用里面的属性，

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog('大黄', 3)
# dog1.gender = '男' 没使用__slots__魔法之前，属性不存在则也会自动添加属性，使用魔法以后，则会报错
