"""---author==hxj---"""
# str1 = input("输入用户名(只能有数字和字母组成,首字母必须是大写字母)：")
# for index in str1:
#     if ('a' <= index <= 'z' or 'A' <= index <= 'Z' or '0' <= index <= '9') and 'A' <= str1[0] <= 'Z':
#         pass
#     else:
#         print("用户名不合格！")
#         break
# print("用户名是：", str1)

# str1 = 'abcd1234'
# print(str1[1::2])
#
# str1 = input("输入用户名(6~10位)：")
# if 6 <= len(str1) <= 10:
#     pass
# else:
#     print("用户名不合法！")
# str1 = 'a2h2klm12小明'
# str1 = input("请输入字符串：")
# for index in str1:
#     if 'a' <= index <= 'z':
#         x = ord(index)
#         y = chr(x - 32)
#         index = y
#     print(index, end='')
# str1 = input("输入字符串：")
# x = int(len(str1)) // 2
# if int(len(str1)) % 2 == 0:
#     print("字符串的中间字符是:", str1[x-1], str1[x])
# else:
#     print("字符串的中间字符是:", str1[x])
# str1 = 'how are you? Im fine, Thank you!'
# print("you在字符串中第一次出现的位置是：", str1.find('you'))
# print("you在字符串中第一次出现的位置是：", str1.index('you'))
str1 = 'abc'
print(str1.center(6, '+'))
