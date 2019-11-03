"""---author==hxj---"""
# 1.列表.append(元素) - 在列表的最后添加一个元素
# 2.列表.insert(下标，元素) - 在列表指定下标前插入一个元素
# 3.列表.pop(下标)   -  取出列表中指定下标对应的元素, 返回被取出的元素
#    列表.pop()      -   取出列表中最后一个元素，返回被取出的元素
# 4.列表.count(元素) -- 统计列表中指定元素的个数
nums = [23, 33, 44, 65, 77, 33, 67, 33]
print(nums.count(33))
# 5.列表.extend(序列) -- 将序列中的元素添加到列表的最后，没有返回值
nums.extend([10, 20])
print(nums)

# 6. 列表.index(元素) -- 获取元素在列表中的正下标（如果元素有多个只取第一个,元素如果不存在，报错）
print(nums.index(33))

# 7.列表.reverse() -- 让列表倒序（不会产生新的列表）
print(nums.reverse())

# 8.排序
# 列表.sort() -- 将列表中的元素从小到大排序
# 列表.sort(reverse=True) -- 将列表中的元素从大到小排序
# 注意：列表的元素类型必须是一样的，并且元素支持比较运算符；不会产生新的列表
# sorted() -- 对序列中的元素从小到大排序，产生一个新的序列
# sorted(序列，reverse=True) -- 对序列中的元素从小到大排序，产生一个新的序列
nums = [23, 33, 44, 65, 77, 33, 67, 33]
nums1 = sorted(nums)
print(nums)
print(nums1)

# 9.清空列表 列表.clear()

# nums.clear()
# print(nums)
#
# # 10.列表.copy() -- 和列表[:]的效果一样，赋值列表中的元素产生一个新的列表，属与浅拷贝。
# nums = [23, 33, 44, 65, 77, 33, 67, 33]
# new_nums1 = nums  # 直接赋值，赋的是地址，对列表操作时，两个列表都会改变
# new_nums2 = nums.copy()  # 产生新的一个列表，操作不会互相影响
# new_nums3 = nums*2  # 只要跟原列表不一样，就不会赋值地址，而是产生新的列表
# print(id(nums))
# print(id(new_nums1))
# print(id(new_nums2))
# print(id(new_nums3))

