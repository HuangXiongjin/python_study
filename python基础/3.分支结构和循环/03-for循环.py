"""---author==hxj"""
# python中有两种循环： for-in循环和while循环
# 1.for循环
"""
1) 语法：
for 变量 in 序列：
    循环体
其他语句

2）说明
for --- 关键字
变量 --- 标识符
in --- 关键字
序列 --- 容器型数据类型的数据，例如：字符串、列表、元组、字典、集合、迭代器、生成器、range
循环体 --- 和for保持一个缩进的一条或者多条语句；循环体种的代码就是需要重复执行的代码

3）执行过程：让变量从序列种一一取值，每取一个值执行一个循环体，直到取完为止。
（python种控制for循环的次数，是通过控制in后面序列元素的个数来控制的）
"""
# for x in 'hello':
#     print(x)
#     print("=====")
# 练习：打印10行“===”
for x in '1111111111':
    print("===")

# 2.range函数---产生指定范围内的数字序列
"""
range(N) --- 产生 0~N-1 次的整数数列
range(M, N) --- 产生 M~N-1 的整数数列
range(M, N, step) --- 从M开始每次加step产生下一个数，直到N的前一个数为止
"""
# for x in range(11):
#     print(x)
#
# for _ in range(11):
#     print("!!!")
#
# for x in range(1, 10):
#     print(x)
#
# for x in range(0, 101, 2):
#     print(x)
"""练习1：计算1+2+3+...+100"""
sum = 0
for num in range(1, 101):
    sum += num
print(sum)

"""练习2：统计100以内能够被2但是不能被3整除的数的个数 """
# 统计个数的套路：
"""
count = 0
for num in range(1, 100):
    if num % 2 == 0 and num % 3 != 0:
        count += 1
        print(num)
print(count)

"""
count = 0
for num in range(0, 100, 2):
    if num % 3 != 0:
        count += 1
print("个数:", count)
