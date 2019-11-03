"""---author==hxj---"""
# 1.迭代器（iter）
"""
迭代器作为容器可以保存多个数据；数据的来源：1）将其他序列转换成迭代器  2）生成器
"""
# 1）将其他序列转换成迭代器:
iter1 = iter('abc')
print(type(iter1))  # <class 'str_iterator'> 字符串迭代器
iter2 = iter([1, 2, 3])  # <class 'list_iterator'> 列表迭代器
print(type(iter2))

# 2）获取元素
"""
不管用哪种方式获取元素的值，那么这个元素在迭代器中就不存在了
1）获取单个元素：next(迭代器)、迭代器.__next__() --- 获取迭代器中的第一个元素
2）遍历: 
for 变量 in 迭代器:
    pass
"""
iter3 = iter('hello')
print(next(iter3))
print(next(iter3))
print(next(iter3))
print(iter3.__next__())
print(iter3.__next__())
# print(iter3.__next__())  # StopIteration 如果迭代器为空报错
iter4 = iter('world')
for x in iter4:
    print(x)
