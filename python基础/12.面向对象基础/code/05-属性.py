"""---author==hxj---"""
# 1.类中的属性
"""
属性就是声明在类中的的 变 量；类中的属性分为：字段；对象属性

1）字段
a.怎么声明：声明在类中的里面函数的外面的变量就是字段
b.怎么使用：通过类去使用，以“类.字段”的形式去使用
c.什么时候用：属性的值不会因为对象不同而不同，这样的属性就声明成类的字段

"""


class Person:
    num = 100  # num的属性就是字段

    def func1(self):
        a = 10
        print(Person.num)
        pass


Person().func1()
print(Person.num)
Person.num = 2000
print(Person.num)
print("=====================对象属性=========================")
"""
2）对象属性（重要）
a.怎么声明：以“self.属性值=值”的形式声明在__init__方法中
b.怎么使用：通过对象去使用，
c.什么时候用：属性的值可能会因为对象不同而不一样，这样的属性就声明成对象属性
"""


# class Student:
#     def __init__(self):
#         # 这的name,age,gender,study_id就是对象属性
#         self.name = '张三'
#         self.age = 20
#         self.gender = '男'
#         self.study_id = 'stu001'
#
#
# stu1 = Student()  # 创建对象
# print(stu1.name, stu1.age, stu1.gender, stu1.study_id)
# stu1.age = 18
# print(stu1.name, stu1.age, stu1.gender, stu1.study_id)


class Student2:
    def __init__(self, name, study_id, gender='男'):
        self.name = name
        self.study_id = study_id
        self.gender = gender
        self.age = 18


stu3 = Student2('小花', '002', '女')
print(stu3.name, stu3.age, stu3.gender, stu3.study_id)
stu3 = Student2('小花', '002')
print(stu3.name, stu3.age, stu3.gender, stu3.study_id)


class Dog:
    def __init__(self, name, breed, age=12, gender='母'):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed

    def print_message(self):
        print(self.name, self.age, self.gender, self.breed)

    def cry_type(self, name, cry):
        self.name = name
        self.cry = cry
        print(name + ' 是 ' + cry + ' 的叫')


dog1 = Dog('旺财', age=10, gender='公', breed='土狗')
dog1.print_message()
dog1.cry_type('旺财', '汪汪汪')



