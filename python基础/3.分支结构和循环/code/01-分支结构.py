"""---author==hxj"""
# python中的分支结构只有if语句
# 1.if语句
"""
1)结构1：满足某个条件才执行某段代码
a。语法
if 条件语句：
    代码段
其他语句

b.说明：if - 关键字
    条件语句 - 可以是一个具体的数据，也可以是一个已经赋值过的变量，或者是运算表达式（不能是赋值语句）
    ：- 固定写法
    代码段 - 一条或者多条和if语句保持缩进的任何语句

c.执行过程：先判断条件语句的结果为是否位True（如果不是布尔就先转换成布尔），如果为True就执行代码段，在执行其他代码段，否则直接执行其他语句
补充：布尔值转换 - python中的所有的数据都能转换成布尔，所有为0为空的值都会转换成False, 其他都是True
"""
if False:
    print('2343')
    print('23')
print('54')

if -100:
    print('333')
print('12')

if 100:
    print('344')
print('1235')

num = int(input('请输入一个整数：'))
if num & 1 == 0:
    print('偶数')
print('奇数')
"""
a.语法：
if 条件语句：
    代码段1
else:
    代码段2
b.说明
if /else - 关键字
条件语句 - 
"""
num = int(input('请输入一个整数：'))
if num & 1 == 0:
    print('偶数')
else:
    print('奇数')
"""
3)结构啊3: 条件有多个（有关联）的时候执行不同的代码段（if-elif-elif-...-else）
a.语法
if 条件语句1：
    代码段1
elif 条件语句2：
    代码段2
.。。
else:
    代码段N
b.执行过程：按顺序判断条件语句是否为True,如果为True就执行该条件语句的代码段，
满足则跳出结构，不满足则往下继续判断。
"""
age = int(input('请输入年龄（0~150):'))
if age <= 3:
    print("youer")
elif 4 <= age <= 12:
    print("ertong")
elif 13 <= age <= 18:
    print("qingshaonian")
elif 19 <= age <= 28:
    print("qingnian")
elif 29 <= age <= 50:
    print("zhuangnian")
else:
    print("laonian")

# 2.if语句嵌套
# 在if结构中的if、else、elif后面的代码段中，还可以写其他的if语句
# 练习：输入一个数，如果这个数是偶数，打印‘偶数’，如果是奇数打印‘奇数’，如果这个数能被4整除就打印“4的倍数”
num = int(input("shu:"))
if num & 1 == 0:
    print("偶数")
    if num  % 4 == 0:
        print('4的倍数')
else:
    print('奇数')
