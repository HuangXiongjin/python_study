"""---author==hxj---"""
# 1.变量的作用域: 变量在程序中能够使用的范围
# 2.全局变量和局部变量
"""
1)全局变量: 没有声明在函数里面或者类里面的变量就是全局变量;
           作用域是从声明开始到文件结束的任何位置
2)局部变量: 声明函数中的变量就是局部变量(函数的参数相当于声明在函数中的变量)
           作用域是从声明开始到函数结束的任何位置
           
3）函数调用过程(内存): 压栈
当调用函数的时候， 系统会自动在内存的栈区间为这个函数开辟一个独立的内存区域，
用来保存在函数中声明的变量。当函数调用结束这个内存区域会自动释放。
"""
print('==============全局变量================')
a = 10   # 全局变量

# x是全局变量
for x in range(5):
    if False:
        c = 100
    b = 20   # 全局变量
    print('循环里面:', a)
    print('循环里面:', x)

print('外面:', b)


def func1():
    print('函数里面:', a)
    print('函数里面:', x)
    print('函数里面:', b)


func1()

print('===================局部变量===================')


def func2(x1=10, y1=20):
    z1 = 100
    print('函数内部:', x1, y1, z1)


func2()


# print('函数外部:', x1)   # NameError: name 'x1' is not defined
# print('函数外部:', z1)   # NameError: name 'z1' is not defined


# 3. global和nonlocal
"""
global和nonlocal函数中的关键字，和return一样只能在函数体中使用
1)global - 在函数中声明一个全局变量
global 变量
变量 = 值

2)nonlocal: 在局部的局部中去修改局部变量的值
nonlocal 变量
变量 = 值
"""
print('=============global=============')
a1 = 111
b1 = 100


def func3():
    # 这儿是在声明一个局部变量a1
    a1 = 222
    print('函数里面a:', a1)

    # 这儿的b1是全局变量
    global b1
    b1 = 333
    print('函数里面b:', b1)


func3()

print('函数外面a:', a1)
print('函数外面b:', b1)

print('================nonlocal=============')


def func4():
    a2 = 100

    def func5():
        nonlocal a2
        a2 = 500
        print('函数里面的函数里面a2:', a2)

    func5()

    print('函数里面a2:', a2)


func4()
# print(a2)    # NameError: name 'a2' is not defined


def func(str):
    # str = 'abc'
    sum = 0


func('hello world!')

print(str(100))