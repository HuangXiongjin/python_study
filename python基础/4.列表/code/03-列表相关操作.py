"""---author==hxj---"""
# 1.列表的数学运算：+ ， *
# 列表1 + 列表3 ---将两个列表中的元素合并产生一个新的列表（不会修改原列表）
print([1, 2, 3] + [10, 20, 30])  # [1, 2, 3, 10, 20, 30]
list1 = [11, 22, 33]
print(list1 + [100, 200], list1)

# 列表 * N、 N*列表  --- N是正整数，列表中产生
list2 = [11, 22, 33]
print(list2 * 3, list2)  # [11, 22, 33, 11, 22, 33, 11, 22, 33] [11, 22, 33]

# 2.列表的比较运算：==，!=
# 列表1 == 列表2；列表1 != 列表2
list2 = [1, 2, 3]
list3 = [1, 2, 3]
print(list2 == list3)   # True
list3 = [1, 3, 2]
print(list2 == list3)   # False

# 比较相等
"""
补充：is的用法
== ：判断两个数据的值是否相等
is ：判断两个数据的地址是否相等
list2 = [1, 2, 3]
list3 = [1, 2, 3]
list4 = [1, 4, 3]
print(list2 == list3)   # True
print(list2 is list3)   # True
print(list2 is list4)   # False
"""
# 比较大小
print([1, 2, 3, 4, 5] > [1, 3])  # False
print([2, 2, 3, 4, 5] > [1, 3])  # True
print([1, 2, 3, 4, 5] > [3, 2])  # False

# 3. in 和 not in
"""
元素 in 列表 --- 判断元素是否在列表中
元素 not in 列表 --- 判断元素是否不在列表中
"""
print(60 in [20, 45, 60])  # True
print(25 in [20, 45, 60])  # False

# 4.内置函数：max(序列) , min(序列) sum(序列), len(序列), list(序列)
'''
max 和 min要求序列中的元素类型必须一致；并且元素支持比较运算符
sum要求序列中的元素必须是数字
list(序列) -- 只有容器型数据类型才能转换成列表;将序列中的元素作为列表的元素产生一个新的列表
'''

list1 = [1, 2, 3, 4]
# list1 = ['小明', '小花', 'ABC']
print(max(list1))
print(min(list1))
print(sum(list1))
print(len(list1))
print(list('abcd'))
print(list(range(10)))
