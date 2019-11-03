"""---author==hxj---"""
"""
1.list 
容器：可变的，有序的

2.元素
[元素1，元素2，元素3]

3.增删改查
查 --- 1）获取单个元素：列表[下标]
        2）切边：列表[开始下标：结束下标：步长]
        3）遍历

增 --- 列表.append(元素)；列表.insert(下标，元素)
删 --- del 列表[下标]；列表.remove(元素)；列表.pop()/列表.pop(下标)
改 --- 列表[下标] = 新值
"""
list1 = [1, 2, 3, 8, 4, 6]
for index in range(0, len(list1)):
    list1[index] = list1[index] * 2
print(list1)