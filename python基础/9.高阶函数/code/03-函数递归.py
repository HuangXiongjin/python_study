"""---author==hxj---"""
# 1.什么是递归函数
"""
自己调自己的函数(函数体中调用当前函数)
循环能做的事情，递归都可以做

注意: 能用循环解决的问题就不要用递归
"""


# def func1():
#     print('=====')
#     func1()
#
#
# func1()

# 2.怎么写递归函数
"""
第一步: 找临界值(循环结束的条件) - 在这儿需要结束函数
第二步: 找关系 - 找f(n)和f(n-1)的关系(找当次循环和上次循环的关系)
第三步: 假设函数的功能已经实现,根据关系用f(n-1)去实现f(n)的功能
"""
# 用递归函数实现: 1+2+3+...+n
def sum1(n):
    # 第一步: 找临界值
    if n == 1:
        return 1
    # 第二步: sum1(n)和sum1(n-1)
    # sum1(n) == 1+2+3+...+n-1+n
    # sum1(n-1) == 1+2+3+ ... + n-1
    # sum1(n) = sum1(n-1) + n
    return sum1(n-1)+n


print(sum1(100))


# 用递归函数求斐波那契数列中第n个数: 1, 1, 2, 3, 5, 8, 13, 21,...
def sequence(n):
    if n == 1 or n == 2:
        return 1
    # 找关系:sequence(n)和sequence(n-1)
    # sequence(n) = sequence(n-1) + sequence(n-2)
    return sequence(n-1) + sequence(n-2)


print(sequence(1), sequence(2))
print(sequence(8))

# 练习: 用递归实现以下功能
"""
n = 5
*****
****
***
**
*

n=4
****
***
**
*
"""


def print_star(n):
    if n == 1:
        print('*')
        return
    # 找关系: 打印n个*, 再实现f(n-1)的功能
    print(n * '*')
    print_star(n-1)


print_star(3)


# 练习: 用递归实现以下功能
"""
n=3
*
**
***

n=4
*
**
***
****
"""


def star1(n):
    if n == 1:
        print('*')
        return
    print(n*'*')
    star1(n-1)


star1(5)


def star2(n):
    if n == 1:
        print('*')
        return
    star2(n-1)
    print(n*'*')


star2(5)



