"""---author==hxj"""
# 3.逻辑运算符: and(逻辑与运算), or(逻辑或运算), not(逻辑非运算)
# 所有的逻辑运算符的运算对象是布尔，结果也是布尔
"""
1) and
a.运算规则：两个都为True结果才是True
True and True -> True
True and False -> False
False and True -> False
False and False -> False

b.什么时候用：当希望多个条件同时满足的时候，就用and将多个条件连接。
"""
# 用一个变量保存学生的绩点，一个变量保存学生的操评分；写一个条件来判断学生是否能拿奖学金
# 1）奖学金条件：绩点不低于3.5，操评分至少90分
# 条件1：grade >= 3.5 score >= 90
grade = 4
score = 98
print("是否能拿奖学金：", grade >= 3.5 and score >= 90)

"""
2) or
a.运算规则：两个都为False结果为False,只要一个结果是True结果就是True
True and True -> True
True and False -> True
False and True -> True
False and False -> False
b. 什么时候用：当希望多个条件只要有一个满足的时候，就用or将多个条件连接，相当于生活中的或者
"""
# 用一个变量保存学生的绩点，一个变量保存学生的操评分；写一个条件来判断学生是否能拿奖学金
# 1）奖学金条件：绩点不低于4.0，操评分至少95分
# 条件1：grade >= 4.0 score >= 95
grade = 2
score = 98
print("是否能拿奖学金：", grade >= 5 or score >= 100)

# 练习1：
num = int(input("输入数："))

# 1）判断一个数是否能够被2整除或者5整除
print(num % 2 == 0 or num % 5 == 0)

# 2）判断一个数是否能够同时被2整除或者5整除
print(num % 2 == 0 and num % 5 == 0)

# 3）判断一个数是否是3或者7的倍数，并且这个数的末尾不是3
print((num % 3 == 0 or num % 7 == 0) and (num % 10 != 3))

"""
3) not
a. 运算规则：True变False,False变成True
not True -> False
not False -> True
b.什么时候用：对某个条件进行否定
年龄不在12-18岁:not 12 <= age <= 18

4) 短路操作
逻辑与运算的短路操作：当and前面的表达式的值出现False的时候，程序不在执行and后面的表达式
逻辑或运算的短路操作:当or前面的表达式的值出现True的时候，程序不在执行or后面的表达式
def func():
    print("huanshu ")
True and func()
print("====")
"""
# 4.赋值运算服：= , +=, -=, *=, /=, %=, //=, **=
"""
不管是什么样的赋值运算符，最终的操作都是给变量赋值；所以赋值运算符的左边必须是变量
1）= ：将右边的值赋给左边的变量
2）复合的赋值运算符：先将赋值符号左边的变量中的值取出来，然后进行指定的运算，最后将计算出来的值重新赋给左边的变量

"""
