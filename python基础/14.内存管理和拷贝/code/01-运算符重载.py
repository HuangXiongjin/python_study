"""---author==hxj---"""
# 1.运算符
"""
python中所有的类型都是类，所以所有的数据都是对象；python中使用的任意运算符都是在调用相应类中的相应的方法，
每一个运算符对应什么方法都是固定的。某种数据是否支持某个运算符就看这个数据类型中是否实现了对应的方法
"""
# 2.运算符重载指的是在不同的类中实现同样的运算符对应的函数
"""
默认情况下，类的对象支持 ==， !=

"""


class Student:
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score

    def __repr__(self):
        return '<%s, id:%s>' % (str(self.__dict__)[1:-1], hex(id(self)))

    # a+b ->  a.__add__(b)
    # self -> 当前类的对象，也是+前面的那个数据
    # other -> +后面的那个数据, 类型根据运算规则的设计可以是任何类型的数据
    def __add__(self, other):
        # return self.age + other.age
        return self.score + other.score
        # return Student(self.name+other.name, self.age+other.age, self.score + other.score)
        # return self.score + other

    # a*b -> a.__mul__(b)
    def __mul__(self, other):
        list = []
        for _ in range(other):
            list.append(copy.copy(self))
        return list

    # a<b  -> a.__lt__(b)
    # 注意: <和>符号只需要重载其中一个就可以
    def __lt__(self, other):
        return self.score < other.score


stu1 = Student('小明', 19, 90)
stu2 = Student('小花', 20, 78)

# stu1.__add__(stu2)
print(stu1 + stu2)

# stu1.__add__(100)
# print(stu1 + 100)

print(stu1 * 2)  # [<'name': '小明', 'age': 19, 'score': 90, id:0x16c61f4ed68>,
                   # <'name': '小明', 'age': 19, 'score': 90, id:0x16c61f4ea20>]

# students = [stu1, stu2, Student('小红', 12, 100)]
# students.sort()
# print(students)
#
# print(stu1 < stu2)
# print(stu1 > stu2)