"""---author==hxj---"""
import copy
# lanlianhua.txt. 直接赋值

# 3.浅拷贝
"""
字符串、列表和元组的切片；对象.copy();copy模块中的copy方法都是浅拷贝
浅拷贝只会拷贝当前对象，不会拷贝当前对象的子对象
"""
# list1 = [lanlianhua.txt, 2, 3]
# list2 = copy.copy(list1)
# list3 = copy.deepcopy(list1)
# print(id(list1), id(list2), id(list3))


# 4.深拷贝
"""
copy模块中的deepcopy方法是深拷贝
"""
a = ['color', 'heigth', 'blackground']
b = [a, 'aaa', 'bbb']
c1 = b  # [a, 'aaa', 'bbb']
print(c1)
c2 = copy.copy(b)  # [a, 'aaa', 'bbb']
c3 = copy.deepcopy(b)  # [a, 'aaa', 'bbb']
a[-1] = ['BG']  # ['color', 'heigth', 'BG']
b.append('ccc')  # [a, 'aaa', 'bbb', 'ccc]
print(c1)
print(c2)
print(c3)
