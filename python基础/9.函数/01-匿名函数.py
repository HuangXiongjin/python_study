"""---author==hxj---"""
# 1.匿名函数
"""
匿名函数就是没有函数名的函数,属于function类型的数据
注意：匿名函数本质还是函数，函数中除了声明语法以外，其他的都使用匿名函数

1）语法
lambda 参数列表：返回值

2）说明
lambda -- 关键字
参数列表 -- 参数名1，参数名2
： -- 固定
返回值 - 任何有结果的表达式；它匿名函数的函数体，相当于普通函数中的return语句
"""


a = filter(lambda x: x > 2, [1, 2, 3, 4])
print(a)
print(lambda x: x > 2, [1, 2, 3, 4])

