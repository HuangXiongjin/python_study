"""---author==hxj---"""
# 1.getter和setter
"""
当我们需要在获取属性值之前做点别的事情，就需要给这个属性添加getter;
当我们需要在给属性赋值之前做点别的事情，就需要给这个属性添加setter.
"""
# 2.给属性添加getter
"""
1)属性命名的时候前面加“_”
2)在装饰器@property后面声明一个对象方法
    a.将属性去掉下划线作为方法名
    b.方法除了self以外不需要其他参数
    c.函数的返回值就是获取这个属性的时候得到的值
3)在外部使用属性的时候，通过“对象.属性(不带下划线的属性)”去使用
注意：获取属性的时候，就会自动取调用getter对应的函数
"""
# 3.给属性添加setter
"""
属性添加setter之前必须先添加getter
1)保证添加属性名之前有“_”
2)在@getter名.setter后面声明对象方法
    a.将属性去掉下划线作为方法名
    b.需要一个self以外的参数
    c.不需要返回值
3)在外部使用属性的时候，通过“对象.属性(不带下划线的属性)”去使用

注意：当属性赋值的时候，实质就是调用setter对应的方法
"""




class Person:
    def __init__(self, name, gender):
        self.name = name
        self._age = 0
        self.gender = gender
        self._week = 0

    @property  # 添加getter的作用
    def week(self):
        if self._week == 0:
            return '星期天'
        elif self._week == 1:
            return '星期一'
        elif self._week == 2:
            return '星期二'
        elif self._week == 3:
            return '星期三'
        elif self._week == 4:
            return '星期四'
        elif self._week == 5:
            return '星期五'
        elif self._week == 6:
            return '星期六'

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int)):  # 判断类型,如果不是指定的类型就报错
            raise TypeError
        self._age = value


p1 = Person('小明', '男')
p1._week = 4
print(p1._week)  # 4
print(p1.week)  # 实质是在调用week方法获取返回值

print("=========================================")
# p1.age = 200
p1.age = '200'
print(p1.age)


# 练习：写一个矩形类
# 属性：长、宽、面积、周长


class rectangle:
    def __init__(self, length, wide):
        self._length = 0
        self._wide = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value


