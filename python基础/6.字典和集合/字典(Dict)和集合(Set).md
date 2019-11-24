# 1. 什么是字典（dict）

1）字典是容器型数据类型（序列），将{}作为容器的标志，元素用逗号隔开
特点：可变（增删改），无序（不支持下标操作）
2）字典中的元素
字典中的元素都是键值对，以"键：值"的形式成对出现
{键1：值1，键2：值2，键3：值3....}
{key1 : value1, key2 : value2, key3 : value3,...}
字典存储数据主要是为了存值，键只是为了区分不同的值而存在的

键值对中的键 - 不可变；唯一的
键值对中的值 - 可变的，和列表元素一样，任何数据都可以作为值
key 是唯一的

# 1.查 - 获取字典的值

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

# 2.增/改

增 - 添加键值对     改 - 修改字典中某个key对应的值
语法： 字典[key] = 值
当key不存在时就在字典中添加该键值对，存在就修改字典中的该键值对

dict2 = {'a': 1, 'b': 3, 'c': 28}
dict2['c'] = 2
print(dict2)

# 3.删 = 删除key的对应的值

1）def 字典[key] -- 删除指定key对应的键值对
2）字典.pop() -- 取出字典中key对应的值；返回被取出的值
dict2 = {'a': 1, 'b': 3, 'c': 28}
del dict2['b']

# 1.相关运算

字典不支持+，*，<,>, <=,>=
支持：== ; !=

print({'a': 10, 'b': 20} == {'a': 10, 'b': 20})  # True
print({'a': 10, 'b': 20} == {'b': 20, 'a': 10})  # True

# 2.相关操作： in / not in ; max / min / sum/ len

 max / min / sum/ -- 针对的是key的操作
 key in 字典 -- 判断字典中是否存在某个键
dict(数据) -- 将指定的数据转换成字典
数据要求：1）数据本身是一个序列
2）序列中元素必须是有且只有两个元素

# 3.相关方法

dict1 = {1: 10, 2: 20, 3: 30}
dict1.clear()
print(dict1)

1)dict1.fromkeys(序列，值1=None) - 创建一个新的字典，将序列中的元素作为字典的key，
将值1作为每个key对应的value
 2)字典.item() -- 将字典转中的键值对转换成元组作为容器中的元素
dict1 = {1: 10, 2: 20, 3: 30}
print(dict1.items())
 3)字典.values(), 字典.key()
print(dict1.values(), dict1.keys())
 4)字典.setdefault(key,value=None) - 在字典中添加键值对，如果存在不会修改
5）字典.update(字典2) -- 将字典2中的键值对全部添加到字典1中

# 1.集合（set）

"""
1）.集合是容器型数据类型（序列）；将{}作为容器的标志，多个元素用逗号隔开
和字典不一样，集合的元素是独立的数据不是键值对
特点：可变（增删）、无序（不支持下标操作）
{1，2，3，4}
注意：单独的{}表示空字典，不是集合

2）元素 -- 不可变的数据；同一个元素只能有一个（）唯一性
"""

# 空集合

set1 = ()
print(type(set1))

set1 = {12, 'abc', (1, 2)}

# 集合自带去重功能

set1 = {1, 1, 3, 5, 5}
print(set1)

scores = [87, 65, 10, 87, 90, 87]
scores = list(set(scores))
print(scores)

# 2.集合元素的增删改查

# 1）查 -- 只支持遍历，不能单独获取具体的元素

names = {'小明', '小黄', '盖伦', '压缩'}
for item in names:
    print(item)

# 2) 增: 集合.add(元素)

 集合.update(序列) -- 将序列中的所有元素添加到集合中
names.add('剑圣')
print(names)
names.update('鳄鱼')  # {'剑圣', '鳄', '盖伦', '小明', '压缩', '小黄', '鱼'}
print(names)

# 3)删除 - 删除元素

 集合.remove(元素) -- 删除集合中指定的元素
names.remove('小黄')
print(names)

# 4)改（集合不支持修改）

set1 = {1, 2, 3, 4, 5, 6}
set2 = {7, 8, 9, 4, 5, 6}

# 5)求并集：集合1 | 集合2 ---将两个集合的元素合并， 并且去重