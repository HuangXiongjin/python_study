"""---author==hxj---"""
# 1.什么是递归函数
"""
自己调用自己的函数，函数体中调用当前的函数
循环能做的事情，递归都可以做（除死循环）
注意：能用循环解决的问题就不用递归
"""
# def func1():
#     print("===========")
#     func1()
#
#
# func1()

# 2.怎么写递归函数
"""
第一步：找到临界值（循环结束的条件），在这需要结束函数
第二部：找关系 ---- 找f(n) 和 f(n-1)的关系/找当次循环和上次循环的关系
第三步：假设函数的功能已经实现，根据关系用f(n-1）去实现f(n)的功能
"""

"""递归函数实现：1+2+3+...+n """


# def sum1(n):
#     # 第一步：找临界值
#     if n == 1:
#         return 1
#     # 第二步：sumi(n-1)和sum1(n)
#     # sum1(n) = sum1(n-1) + n
#     return sum1(n-1)+n
#
#
# print(sum1(100))


"""打印斐波那契数列中的第N个数：1,1,2,3,5,8,13,......."""
# def sequence(n):
#     if n == 1 or n == 2:
#         return 1
#     # 找关系：sequence(n)和sequence(n-1)
#     # sequence(n) = sequence(n-1) + sequence(n-2)
#     return sequence(n-1) + sequence(n-2)
#
#
# print(sequence(5))


def dayin(n):
    if n == 1:
        print("*")
        return
    # 找关系：打印n个*，在实现f(n-1)的功能
    dayin(n - 1)
    print(n*'*')


dayin(3)
