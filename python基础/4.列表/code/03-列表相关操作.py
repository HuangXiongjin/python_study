"""__author__ = YuTing"""
# 1.列表的数学运算: +, *
# 列表1 + 列表2    -   将两个列表中的元素合并产生一个新的列表；（不会修改原列表）
# 列表 * N 、N * 列表   -  N是正整数; 列表中的元素重复N次产生一个新的列表

# 加法运算
print([1, 2, 3] + [10, 20, 30])
list1 = [11, 22, 33]
print(list1 + [100, 200], list1)

# 乘法运算
print(list1 * 3, list1)   # [11, 22, 33, 11, 22, 33, 11, 22, 33]  [11, 22, 33]


# 2.列表的比较运算: ==, !=, >, <, >=, <=
# 列表1 == 列表2 、 列表1 != 列表2
# 两个列表比较大小，不是比较列表的长度，而是比较元素的大小

# 比较相等
list2 = [1, 2, 3]
list3 = [1, 2, 3]
print(list2 == list3)  # True

list3 = [1, 3, 2]
print(list2 == list3)   # False

# 补充：is的用法
"""
== -> 判断两个数据的值是否相等
is -> 判断两个数据的地址是否一样
"""
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)
print(list1 is list2)    # list1 is list2 相当于: id(list1) == id(list2)

a = 10
b = 10
print(id(a), id(b))
print(a == b, a is b)    # True True

# 比较大小
print([1, 2, 3, 4, 5] > [2, 3])   # False


# 3. in和not in
# 元素 in 列表    -    判断列表中是否存在指定的元素
# 元素 not in 列表   -  判断列表中是否不存在指定的元素
print(60 in [23, 45, 12, 70])    # False
print(12 in [23, 45, 12, 70, 12])    # True

# 4. 内置函数: max(序列), min(序列), sum(序列), len(序列), list(序列)
# max和min要求序列中的元素类型必须一致；并且元素支持比较运算符
# sum要求序列中的元素必须是数字
# list(序列) - 只有容器型数据类型才能转换成列表; 将序列中的元素作为列表的元素产生一个新列表
print(max([23, 45, 78, 90, 32, 45]))
print(min([23, 45, 78, 90, 32, 45]))
print(max(['小明', 'abc', '小花']))

print(sum([23, 45, 78, 90, 32, 45]))
print(sum(range(1, 101)))

# print(list(100))   # TypeError: 'int' object is not iterable
print(list('abc'))
print(list(range(5)))



