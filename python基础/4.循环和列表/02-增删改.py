"""---author==hxj---"""
# 1.增加列表中的元素
"""
1)列表.append(元素) ---- 在列表的最后添加一个元素
2)列表.insert(下标，位置) ---- 在列表的下标前插入一个元素
"""

# 2.删除列表中的元素
"""
1)del 列表[下标] --- 删除列表中指定下标对应的元素
2）列表.remove(元素) --- 删除元素中第一个指定的元素
3)列表.pop(下标) --- 取出列表中指定下标对应的元素
  列表.pop() --- 取出列表中最后一个元素
"""
# nums = [1, 2, 3, 4, 2]
# print(nums)
# nums.remove(2)
# print(nums)
# del nums[1]
# print(nums)
# del nums[1:2]
# print(nums)
"""
nums = [1, 2, 3, 4, 2]
a = nums.pop(1)
print(nums)
print(a)
"""

# 3.修改列表中的元素
"""
列表[下标] = 新值

nums = [1, 2, 3, 4, 2]
nums[1] = 9
print(nums)
"""

# 练习：删除分数列表中所有的分数低于60分的成绩
# scores = [78, 56, 40, 66, 70, 12, 45, 59, 90]
# for index in range(len(scores)):
#     if index < 60:
#         def scores.(index)
#     print(scores[index])
#     if i >= 60:
# #         continue
# #     else:
# #         scores1.remove(i)
# #         scores2 = scores1
# # print(scores2)

