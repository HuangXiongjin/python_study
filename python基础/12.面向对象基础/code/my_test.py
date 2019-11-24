# """---author==hxj---"""
# import math


# class Dog:
#     def __init__(self, name, color, age, cry):
#         self.name = name
#         self.color = color
#         self.age = age
#         self.cry = cry
#
#     def cry_type(self):
#         print(self.name + self.cry + '的叫！')
#
#
# class Person:
#     def __init__(self, name, age, dog, way):
#         self.name = name
#         self.age = age
#         self.dog = dog
#         self.way = way
#
#     def walk_the_dog(self):
#         print(self.name + self.way + self.dog + '去遛狗！')
#         print(self.name + self.way + p1.name + '去遛狗！')
#         print(self.name + self.way + p2.dog + '去遛狗！')
#
#
# p1 = Dog('小黄黄', '黄色', 10, '汪汪汪')
# p1.cry_type()
# p2 = Person('大黄黄', age=19, dog=p1.color, way='牵着')
# p2.walk_the_dog()
# # print(p1.name, p1.age, p1.dog, p1.way)


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi*self.radius**2
#
#     def perimeter(self):
#         return 2*math.pi*self.radius
#
#
# circle1 = Circle(4)
# print(circle1.area())
# print(circle1.perimeter())
# class Student:
#     def __init__(self, name, age, sno):
#         self.name = name
#         self.age = age
#         self.sno = sno
#
#     def answer(self):
#         print(self.name, '答到!')
#
#     def show_information(self):
#         print(self.__dict__)
#
#
# student1 = Student('小明', 18, '1002')
# student1.answer()
# student1.show_information()
#
#
# class Class:
#     def __init__(self, students: list, class_name=''):
#         self.students = students
#         self.class_name = class_name
#
#     def add_student(self, student):
#         self.student = student
#         return self.students.append(student)
#
#
# class1 = Class('h1', 'py1904')
# print(class1.add_student('h2'))
#     # def show_student_information(self):
#     #     print(self.students, self.className)
#     #
#     # def add_student(self):
#     #     return
#
#
# Class1 = Class(student=student1.show_student_information(), className='python1905')
# Class1.show_student_information()

# class Student:
#     """学生类"""
#     def __init__(self, name, age, stu_id):
#         self.name = name
#         self.age = age
#         self.stu_id = stu_id
#
#     def answer(self):
#         print(self.name, '到', sep='')
#
#     def show_message(self):
#         print(self.__dict__)
#
#
# stu1 = Student('小明', 20, '001')
# stu1.show_message()
# stu1.answer()

# , id: int, name: str, age: int


# class Student:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#
#     def to_dict(self):
#         return dict(self)
#
#     def keys(self):
#         return ['id', 'name', 'age']
#
#     def __getitem__(self, item):
#         return getattr(self, item)
#
#
# class Class:
#     def __init__(self, class_name: str):
#         self.class_name = class_name
#         self.students = []
#
#     def add_student(self, student: Student):
#         self.students.append(student)
#
#
# s1 = Student(1, '小名', 18)
# s2 = Student(2, '小红', 19)
# s3 = Student(3, '小黄', 18)
#
# c1 = Class('一班')
#
# c1.add_student(s1.to_dict())
# c1.add_student(s2.to_dict())
# c1.add_student(s3.to_dict())
# print(c1.class_name, c1.students)
# class Classes:
#     def __init__(self, student, class1):
#         self.student = student
#         self.class1 = class1
#
#     def add_student(self):
#         with open('files/students', 'a', encoding='utf-8') as f:
#             f.write(self.student)
#             f.write(self.class1)
#
#     def del_student(self):
#         with open('files/students', '', encoding='utf-8') as f:
#             f.__delattr__(self.student)
#
#
# Class_stu1 = Classes('张三', 'Class 1')
# Class_stu2 = Classes('李四', 'Class 2')
# Class_stu1 = Classes('王五', 'Class 1')
# Class_stu2 = Classes('赵六', 'Class 2')
#
# Class_stu1.add_student()
# Class_stu2.add_student()
#
# Class_stu1.del_student()
class Students:
    def __init__(self, name, age, study_id):
        self.name = name
        self.age = age
        self.study_id = study_id

    def display(self):
        list1 = {'姓名:': self.name, '年龄:': self.age, '学号:': self.study_id}
        return list1


class Classroom:
    def __init__(self, student_name, class_name):
        self.student_name = student_name
        self.class_name = class_name

    def add_student(self, a_class_name, new_message):
        list2.append(new_message)
        dict1[a_class_name] = list2
        print(dict1)

    def del_student(self, class_name, del_name):
        dict1[class_name].remove(del_name)

    def call_roll(self, all_students):
        print(all_students)

    def average_age(self, all_age, all_message):
        sum = 0
        count = 0
        for char in all_age[all_message]:
            sum += char['年龄:']
            count += 1
        return sum / count


dict1 = {}
list2 = []

c1 = Classroom(dict1, '一年级1班')

s1 = Students('小明', 16, '0001')
c1.add_student(c1.class_name, s1.display())

s2 = Students('小红', 18, '0002')
c1.add_student(c1.class_name, s2.display())

s3 = Students('小花', 17, '0003')
c1.add_student(c1.class_name, s3.display())

# c1.del_student(c1.class_name, s3.display())
#
# c1.call_roll(c1.student_name)
#
# print(c1.average_age(c1.student_name, c1.class_name))