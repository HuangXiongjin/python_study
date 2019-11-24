"""---author==hxj---"""
# 1.获取字符串
str1 = 'hello world'
# 1）获取单个字符
# print(str1[0])
# print(str1[-1])

# 2.字符串切片
# print(str1[2:6:2])
# print(str1[3::-1])

# 3)遍历
# for char in 'abc':
#     print(char)
#
# str2 = 'How Are You! Im Fine, THANK YOU!'
# count = 0
# for x in str2:
#     if 97 <= ord(x) <= 122:
#         count += 1
#         print(x, end=" ")
# print(count)

# 2.字符串操作
# 1）+ 和 *
str1 = 'abc'
str2 = '123'
print(str1 + str2)  # abc123
print(str1 + ':' + str2)  # abc:123
print(str1 * 2)  # abcabc
print(2 * str2)  # 123123

# 2) == , !=
print(str1 == str2)  # False

# 3) >,<,>=,<=
# 只能两个字符串比较大小(从前往后按顺序相比较编码值的大小)
# '0' <= char <= '9'  判断是否是数字字符
# 'a' <= char <= 'z'  判断是否是小写字母
# 'A' <= char <= 'Z'  判断是否是大写字母
# '\u4e00' <= char <= '\u9fa5'  判断是否是中文
str1 = 'abc'
str2 = '123'
print('abc' > 'bc')  # False   a < b
print('abcf' > 'abca')  # True f > a
print('abdcdgh' > 'bcd')  # False
print("++++++++++++")
# in / not in
# 字符串1 in 字符串2 --- 判断字符串2中是否包含字符串1
str1 = 'abc'
str2 = 'abcde'
str3 = 'adbce'
print(str1 in str2)  # True
print(str1 in str3)  # False
print('ab' in str2)  # False

# 5)len,max,min,sorted,str
# 字符串转换：所有的数据都能转换成字符串，转换的时候是将数据放在引号中
# 注意：转义字符和编码字符的长度都是1
str1 = 'how are\tyou!'
print(len(str1))  # 12
str1 = '\u4e00how are you!'
print(len(str1))  # 13
print(''.join(sorted(str1)))
print(str(100))
print("===================")

# 6)r语法
# 在字符串的最前面加r或者R，可以阻止字符串中所有的转义字符转义
str1 = '\thow\nare\u4e00you!'
print(str1)
str1 = r'\thow\nare\u4e00you!'
print(str1)

# 7)格式字符串
"""
在字符串中用格式占位符表示字符串中不确定的部分
a.语法：包含格式占位符的字符%（数据1，数据2，...）-- （）中的数据个数和类型
要和前面的格式占位符一一对应

b.格式占位符
%s -- 字符串
%d -- 整数
%.NF -- 浮点数，N控制小数点后小数的位数
%c -- 字符（可以将数字转换成字符）
注意：1）所有的数据都可以使用%s来做个占位符
        2）所有的数据都可以使用%s来接收

"""
name = input("请输入姓名：")
age = int(input("请输入年龄："))
gender = input("请输入性别：")
# xx今年xx岁，性别:xx!
message = '%s今年%s岁，性别:%s!'
print('%s今年%s岁，性别:%s!' % (name, age, gender))
print('%s今年%d岁，性别:%s!' % (name, age, gender))

