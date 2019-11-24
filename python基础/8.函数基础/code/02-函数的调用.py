"""---author---hxj"""

# 1.函数调用过程
"""
1）语法
函数名(实参列表)

2)调用函数的作用: 执行函数体；获取返回值

3)函数调用过程(非常重要!!!!):
第一步: 回到函数声明的位置
第二步: 传参(用实参给形参赋值)
第三步: 执行函数体
(第四步: 执行完函数体就确定返回值)
第五步: 回到函数调用的位置接着往后执行   
"""


# 声明一个函数，实现求1+2+3+...+N的和
def sum1(n):
    # n = 10; n=100
    t = 0
    for num in range(1, n+1):
        t += num
    print(t)


sum1(10)
sum1(100)


# 声明一个函数，实现求m+m+1+m+2+...+N的和
def sum2(m, n):
    # m=10, n=100
    # m=1, n=9
    print('m: %d, n:%d' % (m, n))
    t = 0
    for num in range(m, n+1):
        t += num
    print(t)


sum2(10, 100)
sum2(1, 9)


# 声明一个函数，打印字符串中所有的字母字符
def print_alpha(str1):
    # str1 = 'how are 123 y 90!'
    new_str = ''
    for char in str1:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            new_str += char
    print(new_str)


print_alpha('how are 123 y 90!')


# 声明一个函数，在指定的字符串中数字字符后都添加一个指定的字符
# 'abc123', '*'  ->  'abc1*2*3*'
# 'h2wo4end', '='  -> h2=wo4=end
def append_char(str1, char):
    # str1 = 'abc123', char = '*'
    new_str = ''
    for x in str1:
        if '0' <= x <= '9':
            new_str += x + char
        else:
            new_str += x
    print(new_str)


append_char('abc123', '*')


