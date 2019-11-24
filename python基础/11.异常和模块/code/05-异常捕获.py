"""---author==hxj---"""
# 1.异常捕获
"""
当程序发生异常的时候，默认情况会程序崩溃，不能接着往后执行；捕获异常就是让程序发生异常的时候不崩溃，能够接着往后执行。
一般在明明知道代码可能会出现异常，但是又不能通过修改代码去避免, 这个时候就可以通过异常捕获去处理异常
"""
# age = int(input('请输入年龄(数字):'))
# print(age)

# 2.捕获异常的语法
"""
1)语法一: 捕获所有异常
try:
    代码段1
except:
    代码段2
finally:
    代码段f


说明: try, except  -  关键字，固定写法
     代码段1   -   需要捕获异常的一条或者多条语句
     代码段2   -   出现异常后会执行的一条或者多条语句
     
执行过程: 先执行代码段1,如果执行代码段1的时候出现异常，程序不崩溃，直接执行代码段2；
         如果代码段1没有出现异常，不会执行代码段2


2)语法二:
try:
    代码段1
except 异常类型:
    代码段2
finally:
    代码段f
    
执行过程: 先执行代码段1，如果执行代码段1的时候出现异常，判断异常类型和except后面的异常类型是否一致，
        如果是一致的程序不崩溃，直接执行代码段2；如果不一致，程序直接崩溃
        如果代码段1没有出现异常，不会执行代码段2
        
        
3)语法三:
try:
    代码段1
except (异常类型1, 异常类型2,...):
    代码段2
finally:
    代码段f
    
执行过程: 先执行代码段1，如果执行代码段1的时候出现异常，判断异常类型和except后面的异常类型是否一致，
        如果是一致的程序不崩溃，直接执行代码段2；如果不一致，程序直接崩溃
        如果代码段1没有出现异常，不会执行代码段2

4)语法四:
try:
    代码段1
except 异常类型1:
    代码段11
except 异常类型2:
    代码段22
except 异常类型3:
    代码段33
...
finally:
    代码段f

"""
# 3.finally
"""
捕获异常的最后都可以添加一个finally，finally后面的代码段f任何时候都会执行
1) try后面的代码段没有出现异常，finally会执行
2) try后面的代码段出现异常被捕获到，finally会执行
3) try后面的代码段出现异常没有被捕获到，finally会执行
"""

# 4.抛出异常
"""
让代码在某种情况下主动奔溃:

raise 异常类型
"""


# 异常捕获1
try:
    print({'a': 10, 'b': 20}['c'])
    nums = [1, 2, 3]
    print(nums[4])
    print('==========')
except:
    print('出现了异常!')

# 异常捕获2
print('==========================')
nums = [1, 2, 3]
person = {'name': '小明', 'age': 18, 'gender': '男'}
try:
    print(person['score'])
    print('===')
    print(nums[4])
    print('+++')
except KeyError:
    print('出现键错误的异常!')


# finally
try:
    print(nums[1])
except KeyError:
    print('出现异常')
finally:
    print('写遗书')


# raise
# raise KeyError
class AgeError(Exception):
    def __str__(self):
        return '年龄的值应该在0~150'


age = int(input('输入年龄(0~150):'))
if not 0 < age < 150:
    raise AgeError