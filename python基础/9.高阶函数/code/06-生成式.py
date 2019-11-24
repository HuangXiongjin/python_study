"""---author==hxj---"""
# 1.生成式
"""
生成式就是生成器的简写
1）语法一
（表达式 for 变量 in 序列）
说明： 表达式 -- 任何有结果的语句；数据，赋值后的变量，非赋值的运算表达式等...
展开成生成器：
def 函数名（）
    for 变量 in 序列：
        yield 表达式
"""
# 1.用生成式创建生成器
gen1 = (x*2 for x in 'hello')
print(next(gen1))  # hh
print(next(gen1))  # ee
print(next(gen1))  # ll
print(next(gen1))  # ll
print(next(gen1))  # oo
# print(next(gen1))  # StopIteration

# 2.列表生成式
list1 = list(x for x in range(5))
print(list1)  # [0, 1, 2, 3, 4]

gen2 = (x*10 for x in range(5))
list2 = list(gen2)  # [0, 10, 20, 30, 40]
print(list2)
# print(next(gen2)) #  StopIteration 因为生成式产生的数据已经被转换成了列表

# 3.字典生成式
gen3 = dict((x, x*2) for x in range(5))
print(gen3)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

"""
2)语法二：
生成器 = (表达式 for 变量 in 序列 if 条件语句)
a.展开成函数
def 函数名():
    for 变量 in 序列：
        if 条件语句：
            yield 表达式
            
            
生成器 = 函数名（）

"""
# gen5 = list(x for x in range(10) if x % 2)


def func():
    for x in range(10):
        if x % 2:
            yield x


gen4 = func()
print(list(gen4))  # [1, 3, 5, 7, 9]

"""
三目运算符
C、Java、js等中的三木运算符：变量 = 条件语句？表达式1：表达式2
python中的三目运算符：变量 = 表达式1 if 条件语句 else 表达式2

三目运算符的功能：判断条件语句是否为True,如果是结果是表达式1，否则结果是表达式2

"""
gen6 = list(x % 3 == 0 for x in range(1, 11))
print(gen6)



