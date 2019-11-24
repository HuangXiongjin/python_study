"""---author==hxj---"""
# 1.匿名函数
"""
匿名函数就是没有函数名的函数; 匿名函数可以看成是类型是function的值和10, 'abc'是同类东西
注意: 匿名函数本质还是函数，函数中除了声明语法以外其他的都使用匿名函数

1)语法
lambda 参数列表: 返回值

2)说明
lambda - 关键字
函数名 = 参数列表 - 参数名1,参数名2,...
: - 固定
返回值  -  任何有结果的表达式；它是匿名函数的函数体，相当于普通函数中的return语句

调用匿名函数: 保存匿名函数值的变量(实参列表)

3)参数
普通函数中除了用'参数名:类型'的形式来指定参数类型以外，其他的语法匿名函数都支持
"""

# def 函数名(参数列表):
#     函数体
fn1 = lambda x, y: x + y
"""相当于
def fn1(x, y):
    # x=10, y = 30
    return x+y
"""
fn2 = lambda x: print('====')
"""相当于
def fn2(x):
    return print('=====')
"""

print(fn1(10, 30))
print(fn2(10))

100  # int类型的数据
'abc'  # str类型的数据
[1, 2, 3]  # list类型的数据
{'a': 10, 'b': 20}  # dict类型的数据
lambda x: x  # function类型的数据

a = 100
str1 = 'abc'
list1 = [1, 2, 3]
dict1 = {'a': 10, 'b': 20}
fn1 = lambda x: x
print(a + 10, str1.replace('a', 'A'), list1[0], fn1(90))

list2 = [100, 'abc', [1, 2, 3], lambda x: x * 2]
print(list2)
print(list2[0] * 10)
print(list2[1][0])
print(list2[-1](12))

sum1 = lambda x, y, z=3: x + y + z
sum3 = lambda *nums: sum(nums)


def sum2(x, y, z=0):
    return x + y + z


print(sum2(10, 30), sum2(y=20, x=10))
print(sum1(1, 2), sum1(y=2, x=1))
print(sum3(1, 2, 3, 4, 5))
