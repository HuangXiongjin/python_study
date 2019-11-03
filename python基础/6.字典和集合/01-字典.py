"""---author==hxj---"""
# 1. 什么是字典（dict）
"""
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
"""
dict1 = {'x': 200, (1, 2): 'abc'}
print(dict1)
# dict1 = {'x': 200, [1, 2]: 'abc'}
# print(dict1)  # TypeError: unhashable type: 'list'
dict1 = {'x': 200, 'y': 300, 'x': 120}
print(dict1)  # {'x': 120, 'y': 300}
class1 = {'name': 'python1904',
          'address': '19楼1教室',
          'head_teacher': {
              'name': '张莉萍',
              'tel': '29138294842',
              'QQ': '3478475'
          },
          'all_student': [
              {'name': '小明', 'age': 20, 'study_id': 'qf001'},
              {'name': '小王', 'age': 23, 'study_id': 'qf002'},
              {'name': '小白', 'age': 22, 'study_id': 'qf003'},
              {'name': '小李', 'age': 19, 'study_id': 'qf004'},
              {'name': '小赵', 'age': 24, 'study_id': 'qf005'},
          ]
          }
print(class1)

