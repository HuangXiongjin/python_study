"""---author==hxj---"""
import time


# def sum1(x, y):
#     start = time.time()
#     print('和:', x+y)
#     end = time.time()
#     print('总时间:', end-start)
#
#
# sum1(100, 200)
#
# def decorator(fn):
#     def test(*args, **kwargs):
#         return fn(*args, **kwargs) + 100
#     return test
#
#
# @decorator
# def func1():
#     return 10
#
#
# print(func1())


# def password(fn):
#     def test(*args, **kwargs):
#         ps = input('请输入密码:')
#         if ps == '321':
#             fn(*args, **kwargs)
#     return test
#
#
# @password
# def func3():
#     print('函数3')
#
#
# func3()
# def decorator(func):
#     def test(*args, **kwargs):
#         flag = input("True或者False：")
#         if flag == 'True':
#             return func(*args, **kwargs) + 100
#         elif flag == 'False':
#             return func(*args, **kwargs) - 100
#     return test
#
#
# @decorator
# def fun1():
#     return 5
#
#
# print(fun1())
# def tag(func):
#     def test(*args, **kwargs):
#         return '<p>' + func(*args, **kwargs) + '<p>'
#     return test
#
#
# @tag
# def render2():
#     return 'abc'
#
#
# print(render2())
#
#
# @tag
# def render(text):
#     return text
#
#
# print(render('Hello'))
list1 = [1, 2, 3, 5, 6]
for x in list1[-3:]:
    print(x)
