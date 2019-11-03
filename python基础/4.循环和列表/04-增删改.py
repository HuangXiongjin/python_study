"""__author__ = YuTing"""
# 1.增(增加列表中的元素)
"""
1)列表.append(元素)  - 在列表的最后添加一个元素
2)列表.insert(下标, 元素)  - 在列表指定下标前插入一个元素
"""
films = ['复仇者联盟', '钢铁侠', '哈利波特', '沉默的羔羊', '肖生克的救赎', '恐怖游轮', '辛特勒的名单']
films.append('摔跤吧爸爸')
print(films)
print(films.append('哈尔的移动城堡'))   # None
print(films)

films.insert(1, '千与千寻')
print(films)

films.insert(0, '喜羊羊和灰太狼')
print(films)

# 2.删(删除列表中的元素)
"""
1) del 列表[下标]  - 删除列表中指定下标对应的元素(下标不能越界)
2) 列表.remove(元素)   -  删除列表中的一个指定元素
3) 列表.pop(下标)   -  取出列表中指定下标对应的元素, 返回被取出的元素
   列表.pop()      -   取出列表中最后一个元素，返回被取出的元素
"""
films = ['复仇者联盟', '钢铁侠', '哈利波特', '沉默的羔羊', '肖生克的救赎', '恐怖游轮', '辛特勒的名单']
del films[2]
print(films)
# 下标不能越界
# del films[10]    # IndexError: list assignment index out of range

nums = [12, 89, 90, 89, 67]
nums.remove(89)   # [12, 90, 89, 67]
print(nums)
# 元素必须存在
# nums.remove(100)   # ValueError: list.remove(x): x not in list

films = ['复仇者联盟', '钢铁侠', '哈利波特', '沉默的羔羊', '肖生克的救赎', '恐怖游轮', '辛特勒的名单']
del_film = films.pop()
print(films, del_film)

del_film = films.pop(1)
print(films, del_film)


# 3. 改(修改列表中元素的值)
"""
列表[下标] = 新值
"""
films = ['复仇者联盟', '钢铁侠', '哈利波特', '沉默的羔羊', '肖生克的救赎', '恐怖游轮', '辛特勒的名单']
films[0] = '蜘蛛侠'
print(films)

# 下标不能越界
# films[10] = '教父'   # IndexError: list assignment index out of range


# 练习: 删除分数列表scores中所有分数低于60分的成绩
scores = [78, 66, 40, 66, 70, 12, 45, 59, 90]    # [78, 66, 70, 90]
scores = [x for x in scores if x != 66]
print(scores)

