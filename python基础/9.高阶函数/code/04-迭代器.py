"""---author==hxj---"""

# 1.迭代器(iter)
"""
迭代器作为容器可以保存多个数据；数据的来源: 1)将其他序列转换成迭代器  2)生成器
"""
# 1)将其他序列转换成迭代器
iter1 = iter('abc')
print(iter1, type(iter1))

iter2 = iter([12, 30, 90])
print(type(iter2))

# 2.获取元素
"""
不管用那种方式去获取了元素的值，那么这个元素在迭代器中就不存在了
1)获取单个元素：next(迭代器)、迭代器.__next__() -> 获取迭代器中的第一个元素
2)遍历: 
for 变量 in 迭代器:
    pass
"""
iter3 = iter('hello')
print(next(iter3))
print(next(iter3))
print(next(iter3))
print(iter3.__next__())

# for x in range(100):
#     print(x)

print(next(iter3))
# print(next(iter3))   # StopIteration  如果迭代器为空，用next获取元素的时候会报错

iter4 = iter('world')
for x in iter4:
    print(x)

# print(next(iter4))    # StopIteration

print('===============')
iter4 = iter('world')
print(next(iter4))

for x in iter4:
    print('循环:', x)


