"""---author==hxj---"""

# def max_num(x, y, z):
#     print("最大的数是：", max(x, y, z))
#
#
# max_num(300, 5, 89)


# def function1(num):
#     for index in num:
#         if 'a' <= index <= 'z' or 'A' <= index <= 'Z':
#             print(index, end=' ')
#
#
# function1(input("请输入字符："))
#
#
# def function2(num):
#     for index in num:
#         if '0' <= index <= '9':
#             index += '*'
#             print(index, end='')
#         else:
#             print(index, end='')
#
#
# function2('abc123')
# def average_nums(*nums):
#     sums = 0
#     averages = 0
#     for index in nums:
#         sums += index
#     averages = sums/len(nums)
#     print("平均值为：", averages)
#
#
# average_nums(3, 4)


# average_nums(int(input("输入多个数：")))
# def max_num(*z: int):
#     print("最大的数是：", max(*z))
#
#
# max_num(input("数:"))
# # max_num(3, 5, 6, 45, 90, 122)
# def factorial(num):
#     sums = 1
#     for index in range(1, num+1):
#         sums *= index
#     print("%d的阶乘是：%d" % (num, sums))
#
#
# factorial(int(input("输入所求的数：")))
# def max_num(*z: int):
#     print("最大的数是：", max(*z))
#
#
# max_num(input("数:"))
# # max_num(3, 5, 6, 45, 90, 122)
# 1.返回值
"""
返回值就是return关键字后表达式的值（怎么确定函数的返回值）
返回值就是函数调用表达式的值（怎么获取函数的返回值）
（python中所有的函数都有返回值，默认值是None）

1）return
return是函数体中的关键字（只能在函数中使用），作用：结束函数和确定返回值
a.结束函数：执行函数体的时候只要遇到return函数直接结束
b.确定函数返回值：return 返回值（可以是具体的数据，声明过的变量，运算表达式）
函数调用语句就是函数调用表达式，例如：func1(100), max([1,2])
每个调用函数的语句都有结束，这个结束就是调用这个函数得到的返回值

"""
# 2.怎么使用返回值
"""
想要用函数的返回值，就使用函数调用表达式的值
普通数据能做的事情，函数调用表达式都可以做
"""

# 3.什么时候需要返回值
"""
初学者：看实现函数的功能会不会产生新的数据
return 返回值1，返回值2....
"""


# str1 = 'lfhjshf'
# new_str1 = ''
# # for index in str1:
# if 'a' <= str1[0] <= 'z':
#     x = ord(str1[0]) - 32
#     new_str1 += chr(x)
#     for i in str1[1:]:
#         new_str1 += i
#     print(new_str1)
# else:
#     print(str1)
#     str1[0] = chr(str(x))
# print(str1)
# num = (1, 7, 4, 5)
# max_num = 0
# for index in num:
#     if index > max_num:
#         max_num = index
# print(max_num)
# str1 = 'abdsjhf'
# print(str1[-2:])
# def max(num):
#     max_num = 0
#     for index in num:
#         if index > num:
#             max_num = index
#     print(max_num)
#
#
# max('abdabja')
# max([-7, -12, -1, -9])
# import random
#
#
# def dice(*nums):
#     total = 0
#     for num in nums:
#         print("骰子点数是：", num)
#         total += num
#     print("骰子的点和为：", total)
#
#
# dice(random.randint(1, 6), random.randint(1, 6))


# def my_in(num, i):
#     for index in num:
#         if index == i:
#             return True
#     return False
#
#
# my_in((12, 90, 'abc'), 12)
# def my_replace(str1, i, j):
#     new_str = ''
#     for index in str1:
#         if index == i:
#             new_str += j
#             print(new_str, end='')
#
#
# my_replace('how are you? and you?', 'you', 'me')
# def intersection(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     set_intersection = set1 & set2
#     print("交集为：", set_intersection)
#
#
# def union_set(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     set_intersection = set1 | set2
#     print("并集为：", set_intersection)
#
#
# def differentce_set(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     set_intersection = set1 ^ set2
#     print("差集为：", set_intersection)
#
#
# def supplementary_set(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     set_intersection = set1 - set2
#     print("补集为：", set_intersection)
#
#
# intersection([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
# union_set([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
# differentce_set([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
# supplementary_set([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9])
sum1 = lambda num1, num2=0: num1+num2
print(type(sum1))
print(sum1(10, 20))
print(sum1(num2=200, num1=100))
print(sum1(10))
