"""---author==hxj---"""
from re import *
# re_str = r'([0-2]+[0-9]+[0-5]\.[0-2]+[0-9]+[0-5]\.[0-2]+[0-9]+[0-5]\.[0-2]+[0-9]+[0-5])'
# result = fullmatch(re_str, '255.189.089.009')
# print(result)

# re_str = r'(([0-2]|[0-5][0-5]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5])|' \
#          r'([0-1]|[0-9][0-9]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5]\.[0-2][0-5][0-5])'
# result = fullmatch(re_str, '255.123.054.005')
# print(result)
# re_str = r'\d+\.?\d*'


# def Login():
#     username = input("请输入用户名：")
#     QQ = input("请输入QQ号：")
#     re_str1 = r'[a-zA-Z\d_]{6,20}'
#     re_str2 = r'[1-9][0-9]{4,11}'
#     result1 = fullmatch(re_str1, username)
#     result = fullmatch(re_str2, QQ)
#     if not result1:
#         print('用户名必须由字母、数字或下划线构成且长度在6~20个字符之间')
#     if not result:
#         print('QQ号是5~12的数字且首位不能为0')
#     else:
#         print('登录成功！')
#
#
# Login()

# re_str = r'a.+?的'
# print(search(re_str, '你a好啊发你的伙食费'))
# print(search(re_str, 'hsjsa==2-32'))
# print(search(r'a\d{3,5}?', '你哈a34590876'))

# re_str = r'abc0*123'
# print(fullmatch(re_str, 'abc0000123'))
# str1 = 'hello90abc 78sjh12.5 23.6'
# # str2 = '是234hu士大夫345mmks89h-=数348kl几十块的'
# re_str = r'\d+\.?\d*'
# all_nums = findall(re_str, str1)
# print(all_nums)
# result = split(r'\d+', '爱好3ja89是电话费899将括号看0===三等奖9数据98=的')
# print(result)
# re_str = r'\d+\.?\d'
# 0-99 \d\d
# num1 = '\d|\d\d|1[0-9][0-9]|2[0-5][0-5]|2[0-4][0-9]'
re_str = r'((\d\d?|1[0-9][0-9]|2[0-5][0-5]|2[0-4][0-9])\.){3}(\d\d?|1[0-9][0-9]|2[0-5][0-5]|2[0-4][0-9])'
ip = input("请输入ip地址：")
result = fullmatch(re_str, ip)
print(result)
