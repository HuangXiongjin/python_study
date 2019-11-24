"""---author==hxj---"""
# 1.对齐方式
"""
字符串.center(宽度，填充字符=' '默认空格) -- 居中
字符串.ljust(宽度，填充字符=' '默认空格) - - 左对齐
字符串.rjust(宽度，填充字符=' '默认空格) - - 右对齐
字符串.zfill(宽度) 相当于:字符串.rjust(宽度，0)
"""
str1 = 'abc'
print(str1.center(10, '+'))
print(str1.ljust(9, '='))
print(str1.rjust(9, '='))
print(str1.zfill(9))

num = 12
num1 = 9
print(str(num).zfill(3))  # 012
print(str(num1).zfill(3))  # 009

# 2.统计字串的个数
# 字符串1.count(字符串2) -- 统计字符串1中字符串3出现的次数
str1 = '13429048022'
print(str1.count('2'))
print(str1.count('2', 0, 5))  # 在下标是[0,5)的范围内统计‘2’出现的次数
print("++++++")
print(str1.find('4'))
print(str1.index('4'))

# 6.字符串切割
# 字符串1.split(字符串2) - 将字符串2作为切割点切割字符串1，返回列表
str1 = 'how are you! Im fine, thank you!'
str_list = str1.split(' ')
print(str_list)



