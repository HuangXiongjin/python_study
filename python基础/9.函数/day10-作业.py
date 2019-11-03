"""---author==hxj---"""

"""判断是否闰年"""
#
# def leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         return True
#
#     else:
#         return False
#
#
# year1 = leap_year(2017)
# print(year1)
"""逆序打印列表"""
# dict1 = {'a': 1, 'b': 2}
# dict1['c'] = 3
# print(dict1)


# def study_id_creater(str1, n):
#     return str1.zfill(n)
#
#
# print(study_id_creater('abd', 9))


# def my_items(dict1):
#     new_list = []
#     for index in dict1:
#         list1 = []
#         list1.append(index)
#         list1.append(dict1[index])
#         new_list.append(list1)
#     return new_list
#
#
# print(my_items({'a': 1, 'b': 6}))


# def reverse_print(str1):
#     if len(str1) == 1:
#         return str1[0]
#     return str1[(len(str1)+1)-len(str1)] + str1[len(str1)-len(str1)]
#
#
# print(reverse_print('ljifg'))


# def factorization(num):
# #     i = 2
# #     list1 = []
# #     while i <= num:
# #         if num % i == 0:
# #             list1.append(i)
# #
# #
# # (step(2))
# def reversed_print(str1):
#     length = len(str1)
#     if len(str1) == 1:
#         print(str1)
#     else:
#         print(str1[len(str1)-1], end='')
#         str1 = str1[0: length-1]
#         reversed_print(str1)
#
#
# reversed_print('afdji')
# def factorization(num):
#     i = 2
#     list1 = []
#     if num == 1:
#         list1.append(num)
#     while i <= num:
#         if num % i == 0:
#             list1.append(str(i))
#             num /= i
#         else:
#             i += 1
#     if len(list1) == 1:
#         list1.insert(0, 1)
#     return ' '.join(list1)
#
#
# print(factorization(6))
# list1 = [1, 3, 4]
#
# print(list1)
# print(type(list1[1]))
# a = map(str, list1)
# print(a)
# b = ''.join(list1)
# print(b)
# print(type(a))
# print(type(list1))
# print(type(list1[1]))
def func4():
    for x in range(0, 100, 3):
        yield x


print(next(func4()))
print(next(func4()))
print(next(func4()))
gen4 = func4()
print(next(gen4))   # 0
print(next(gen4))   # 3
print(next(gen4))

