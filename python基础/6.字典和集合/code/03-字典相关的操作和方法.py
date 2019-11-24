"""---author==hxj---"""
# 1.相关运算
"""
字典不支持+，*，<,>, <=,>=
支持：== ; !=
"""
print({'a': 10, 'b': 20} == {'a': 10, 'b': 20})  # True
print({'a': 10, 'b': 20} == {'b': 20, 'a': 10})  # True

# 2.相关操作： in / not in ; max / min / sum/ len

"""
# max / min / sum/ -- 针对的是key的操作
# key in 字典 -- 判断字典中是否存在某个键
dict(数据) -- 将指定的数据转换成字典
数据要求：1）数据本身是一个序列
2）序列中元素必须是有且只有两个元素

"""

print('a' in {'a': 10, 'b': 20})  # True
print(10 in {'a': 10, 'b': 20})  # False

dict1 = {'a': 10, 'b': 20, 'c': 30}
print(max(dict1))
print(min(dict1))
dict1 = {1: 10, 2: 20, 3: 30}
print(sum(dict1))
print(len(dict1))

# 转换
dict1 = {1: 10, 2: 20, 3: 30}

# 3.相关方法
dict1 = {1: 10, 2: 20, 3: 30}
dict1.clear()
print(dict1)
"""
1)dict1.fromkeys(序列，值1=None) - 创建一个新的字典，将序列中的元素作为字典的key，
将值1作为每个key对应的value

"""
new_dict = dict.fromkeys('abc')
print(new_dict)  # {'a': None, 'b': None, 'c': None}
new_dict = dict.fromkeys(range(10, 16), 100)
print(new_dict)

# 2)字典.item() -- 将字典转中的键值对转换成元组作为容器中的元素
dict1 = {1: 10, 2: 20, 3: 30}
print(dict1.items())

# 3)字典.values(), 字典.key()
print(dict1.values(), dict1.keys())

# 4)字典.setdefault(key,value=None) - 在字典中添加键值对，如果存在不会修改
dict1.setdefault('haha', 10)
print(dict1)
dict1.setdefault('haha', 20)
print(dict1)

# 5）字典.update(字典2) -- 将字典2中的键值对全部添加到字典1中
dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {'x': 21}
dict1.update(dict2)
print(dict2)
print(dict1)

dict1.update([(2, 3), (4, 5)])
print(dict1)

dog = {'dog_info': [
           {'name': 'dog1', 'age': 3, 'color': 'black', 'height': 10},
           {'name': 'dog2', 'age': 5, 'color': 'black', 'height': 13},
           {'name': 'dog3', 'age': 2, 'color': 'black', 'height': 15},
           {'name': 'dog4', 'age': 6, 'color': 'black', 'height': 11},
           {'name': 'dog5', 'age': 1, 'color': 'black', 'height': 12},]
      }
# sum = 0
# for value in dog['age']:
#     print(value)
    # sum += value
# print(sum/5)
