"""---author==hxj---"""
# 1.查 - 获取字典的值
"""
1)获取单个元素的值
字典[key] -- 获取字典中指定的key对应的值
字典.get(key)/字典.get(key,默认值) -- 获取字典中指定的key对应的值(如果key不存在返回None或者默认值)；

dog = {'name': '旺财', 'age': 3, 'type': '土狗', 'color': '黄色', 'gender': '母狗'}
print(dog['name'])
print(dog.get('age'))
print(dog.get('weight'))
print(dog.get('weight', 0))


2)遍历
for in ：字典直接拿的是字典中的key
for key in dag:
    print(key, dog[key]) 

（不推荐使用后两种）
for value in dog.values():
    print(value)

for key, value in dog.items():
    print(key, value)   
"""
dog = {'name': '旺财', 'age': 3, 'type': '土狗', 'color': '黄色', 'gender': '母狗'}
for key in dog:
    print(key, dog[key])
for value in dog.values():
    print(value)
for key, value in dog.items():
    print(key, value)

dict1 = {'a': 10, 'b': 30, 'c': 28}
l = dict((value, key) for key, value in dict1.items())
l1 = dict((dict1[key], key) for key in dict1)
print(l)  # 交换key:value
print(l1)  # 交换key:value

# 2.增/改
"""
增 - 添加键值对     改 - 修改字典中某个key对应的值
语法： 字典[key] = 值
当key不存在时就在字典中添加该键值对，存在就修改字典中的该键值对
"""
dict2 = {'a': 1, 'b': 3, 'c': 28}
dict2['c'] = 2
print(dict2)
# 3.删 = 删除key的对应的值
"""
1）def 字典[key] -- 删除指定key对应的键值对
2）字典.pop() -- 取出字典中key对应的值；返回被取出的值
dict2 = {'a': 1, 'b': 3, 'c': 28}
del dict2['b']
"""
dict2 = {'a': 1, 'b': 3, 'c': 28}
# dict2.pop('c')
# print(dict2)
value = dict2.pop('c')
print(value, dict2)