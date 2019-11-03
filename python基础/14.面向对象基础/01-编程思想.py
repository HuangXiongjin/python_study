"""---author==hxj---"""
# 编程思想：面向过程编程(自己造工具实现功能)；函数式编程（用函数去实现功能）；面向对象过程（）
"""
面向过程编程 --- 算法和逻辑
函数式编程 --- 函数
面向对象 --- 类和对象
"""
# =====面向过程=====
# 求1+2+3+4+...+100
sum1 = 0
for x in range(101):
    sum1 += x
print(sum1)

# =====函数式编程=====
# 求1+2+3+4+...+100
print(sum(range(101)))


def sums(n):
    sum2 = 0
    for x in range(n+1):
        sum2 += x
    print(sum2)


sums(100)

# =====面向对象=====
# 求1+2+3+4+...+100


class Math:
    def sums1(self, n):
        sum3 = 0
        for y in range(n+1):
            sum3 += y
        return sum3

    def pro(self, n):
        sum4 = 1
        for z in range(1, n+1):
            sum4 *= z
        return sum4


# ma = Math()
# print(ma.pro(4))
# print(ma.sums1(100))
print(Math().sums1(100))
print(Math().pro(4))
