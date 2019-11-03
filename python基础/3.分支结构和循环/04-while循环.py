"""---author==hxj"""
# 1.while循环
"""
1) 语法：
while 条件语句：
    循环体
2）说明
while --- 关键字
条件语句 --- 只要是有结果的表达式就可以（除赋值语句）
循环体 --- 和while保持一个缩进的一条或者多条语句

3）执行过程
先判断条件语句是否为True,如果为True,就执行循环体；执行完
循环体以后在判断条件语句是否为True,为True又执行循环体，
直到判断条件语句的结果为False的时候，整个循环结束，执行后面的语句

4）for和while循环怎么选择？
for:循环次数确定的时候
while:循环次数不确定和死循环的时候
"""
# i = 1
# while i <= 10:
#     print("hello!")
#     i += 1
# print("h")

count = 0
num = int(input("shuzi:"))
while num != 0:
    num = int(input("shuzi:"))
    if num % 2 == 0:
        count += 1
print("偶数个数为：", count)

