"""---author==hxj---"""
import time

# 1.什么是生成器
"""
1）生成器就是迭代器中的一种
2) 调用一个带有yield关键字的函数就可以得到一个生成器
如果一个函数中有yield关键字:
a. 调用函数不会执行函数体
b. 函数调用表达式的值不是函数的返回值，而是一个生成器对象
"""


# 1.怎么去创建一个生成器
def func1():
    print('=======')
    if False:
        yield
    return 100


gen1 = func1()    # 这儿的gen1就是一个生成器对象
print('外部:', gen1)


# 2.生成器产生数据的原理
"""
1) 一个生成器能够产生多少数据，就看执行完生成器对应的函数的函数体会遇到几次yield;
   yield后面的值就是生成器能够产生的数据
   
2)每次获取生成器中的元素的时候，都是先去执行函数体，直到遇到yield，并且将yield后面的值作为获取元素的结果；
  并且保留结束的位置，下次获取下一个值的时候，从上次结束的位置接着执行函数体，直到遇到yield...
  如果从开始执行到函数结束都没有遇到yield,就会报StopIteration错误
"""
print('================2==========')


def func2():
    print('+++++')
    yield 1
    print('-----')
    yield 100     # yield 后边可以跟数据；同一个函数可以有多个yield


gen2 = func2()
print(gen2)

print('函数外部:', next(gen2))
print('函数外部:', next(gen2))
# print('函数外部:', next(gen2))   # StopIteration


def func3():
    print('第一段代码')
    yield
    print('第二段代码')
    yield
    print('第三段代码')
    yield


gen3 = func3()

time.sleep(1)
next(gen3)
time.sleep(1)
next(gen3)
time.sleep(1)
next(gen3)


# 练习:
def func4():
    # x = 0
    for x in range(0, 100, 3):
        yield x


print(next(func4()))
print(next(func4()))
print(next(func4()))
gen4 = func4()
print(next(gen4))   # 0
print(next(gen4))   # 3
print(next(gen4))

