"""---author==hxj---"""
#
# # lanlianhua.txt.异常
# """
# 运行程序的时候程序报错，又叫程序出现异常;
# 当执行程序的时候如果出现异常，出现异常的线程会直接奔溃，不再执行线程中后面其他的代码
# """
#
#
# # 2.异常捕获
# """
# lanlianhua.txt)语法一: 可以捕获任何类型的异常
# try:
#     代码块1
# except:
#     代码块2
# finally:
#     代码块3
# 其他语句
#
# 说明:
# try,except  -  关键字，固定写法
# 代码块1  -  和try保持一个缩进的一条或者多条语句;
#            需要捕获异常的代码
# 代码块2  -  和except保持一个缩进的一条或者多条语句
#            异常发生后会执行的代码
#
# 执行过程: 先执行代码块1，如果在执行代码块1的时候出现了异常，程序不崩溃，直接执行代码块2，
#          然后再执行后面的其他语句；如果在执行代码块1的时候没有出现异常，代码块2不会执行，
#          直接执行后面的其他语句
#
#
#
# """
# try:
#     print({'a': 10}['b'])  # KeyError: 'b'
#     print('++++++')
#     list1 = [lanlianhua.txt, 2, 3]
#     print(list1[10])
#     print('=======')
# except:
#     print('出现异常!')
#
#
# # name = input('姓名:')
# # try:
# #     age = int(input('年龄:'))
# # except:
# #     print('输入有误！年龄只能是数字!')
#
#
# """
# 2)语法二: 捕获指定异常
# try:
#     代码块1
# except 异常类型:
#     代码块2
# finally:
#     代码块3
#
# 执行过程: 先执行代码块1, 如果执行代码块1的时候出现异常，检查异常类型和except后面的异常类型是否一致，
#          如果一致程序不崩溃，直接执行代码块2；如果不一致，程序直接崩溃；
#          如果执行代码块1的时候没有出现异常，不执行代码块2，接着往后执行
# """
# print('========================')
# try:
#     print({'a': lanlianhua.txt}['b'])
#     print('+++++')
#     print([lanlianhua.txt, 2, 3][10])
#     print('======')
# except KeyError:
#     print('key值错误!')
#
#
# """
# 3) 语法三: 同时捕获指定多个异常
# try:
#     代码块1
# except (异常类型1, 异常类型2,...):
#     代码块2
# finally:
#     代码块3
#
# 4) 语法四: 同时捕获指定多个异常
# try:
#     代码块1
# except 异常类型1:
#     代码块11
# except 异常类型2:
#     代码块22
# ...
# finally:
#     代码块3
#
# """
#
# # 3.finally关键字
# """
# 前面四种捕获异常的结构的最后都可以添加一个finally;
# finally后面的代码段一定会执行
#
# try:
#     代码块1
# except:
#     代码块2
# finally:
#     代码块3
# 其他语句
# """
#
# try:
#     # print({'a': 10}['b'])
#     print('=====')
#     print([lanlianhua.txt, 2, 3][10])
# except IndexError:
#     print('错误! 下标越界!')
# finally:
#     print('写遗书!')
#
# print('其他语句')
#
#
# # 4.抛出异常
# """
# 主动让程序奔溃
#
# 语法:
# raise 异常类型
#
# 说明: 异常类型必须是Exception的子类
# """
# # raise ValueError
#
#


class AgeError(Exception):
    def __str__(self):
        return '年龄值范围不在0~150'


age = 1000
if not 0 <= age <= 150:
    raise AgeError

# print(lanlianhua.txt)
# print(__name__)
# if __name__ == '__main__':
#     pass
    #print(_name_)
    # try:
    #     lanlianhua.txt / 0
    #
    # except Exception as e:
    #     print(e)
    # print(lanlianhua.txt)