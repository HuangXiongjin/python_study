"""---author==hxj---"""
# python中数相关的类型有：int(整型),float(浮点型),bool(布尔),complex(复数)
# 1.int
"""
所有的整数对应的类型就是整型，python3.x中整型对应的数据只有int,python2.x中整型还有long
int(数据) --- 将数据转换成整数，所有的小数，布尔值和部分字符串可以转换成整数（去掉引号以后本身就是一个整数的字符串才能转换成整型）
print(int('12.5')) 不能转换成整型
print(int('12')) 能转换成整型
print(int('+12')) 能转换成整型
print(int('-12')) 能转换成整型
"""

# 2.浮点型
# 所有的小数对应的类型就是浮点型，浮点型对应的数据只有float.支持科学计数法
# float(数据) - 整型、布尔和部分字符串可以转换成浮点型
#               字符串中只有去掉引号本身就是一个数字的字符串才能转换成浮点型
print(float(100))
print(float(True), float(False))
print(float('23'))
print(float('23.8'))

"""
布尔中True本质就是整数1，False本质就是整数0
bool(数据) -- 所有的数据都可以转换成布尔；所有为0为空的值都会转换成False,其他都是True
"""
print(True+1, True*10, False+3, True/10)

# 4.复数
"""
由实部和虚部组成的数字叫做复数：a+bj(a是实部、b是虚部，j是虚数单位)，对应的类型为complex；python直接支持复数的运算
"""
a = 10 + 20j
print(a, type(a))
b = 10 + 1j
c = 10j
print(b, c)
num1 = 2 + 3j
num2 = 4 - 2j
print(num1 + num2)
print(num1 * num2)
print(num1 / num2)

