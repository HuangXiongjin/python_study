"""---author==hxj---"""
# 1.什么是元组（tuple）
"""
1）概念
元组是容器型类型数（序列），将（）作为容器的标志，多个元素用逗号隔开：（元素1，元素2，元素3）
特点：不可改变（不支持增删改），有序的（支持下标操作）

2）元组中元素 -- 和列表要求一样
"""
# 元组的表示
# (), (10), (20,30)
# 1)单个元素的元组：（元素，）必须加逗号
tuple1 = ('abc')
tuple2 = ('abc',)
print(type(tuple1))
print(type(tuple2))

# 2）单独表示一个元组值的时候，小括号可以省略
tuple3 = 1, 2,
print(tuple3)

# 2.获取元组中的元素
"""
列表中获取元素的方式元组都支持
"""
weeks = '周一', '周二', '周三', '周四', '周五', '周六','周天',
# 1)获取单个元素
print(weeks[1])
# print(weeks(2))
# 2)切片
print(weeks[1:4])
print(weeks[1::2])
# 3）遍历
for week in weeks:
    print(week)

for index in range(len(weeks)):
    print(index, weeks[index])
# 4)获取部分元素：变量1，变量2，变量3，....= 元组
# 用变量取获取元组中元素的值（要求前面的变量的个数个元组中元素的个数一致）
tuple1 = (10, 20, 30)  # 列表也可以同样操作
x, y, z = tuple1
print(x, y, z)

# 5）*语法：多个变量某一个变量前* = 元组
# 让不带*的变量去元组中获取元素，剩下的全部给带*的变量(带*的变量会变成一个列表)
student = ('小明', 18, '001', 23, 56, 66)
name, age, study_id, *scores = student
print(name)
print(age)
print(study_id)
print(scores)
print(*scores)
*x, y, z = student
# x, *y, z = student
print(*x)
print(y)
print(z)

# 3.元组相关操作：和列表一样
# +; * ; == ; != ; in ; not in ; max ; min ; sum ; tuple ; len ; sorted
tuple1 = (2, 4, 6, 10, 32)
tuple2 = 3, 5
print(tuple1 + tuple2)
print(tuple1*2)
print(32 in tuple1)
print(34 in tuple1)
print(max(tuple1))
print(sum(tuple1))
print(len(tuple1))
print(sorted(tuple1))
