"""---author==hxj---"""
# 1.变量的作用域：变量在程序中能够使用的范围
# 2.全局变量和局部变量
"""
1)全局变量：没有声明在 函数 里面或者类里面的变量就是全局变量；作用域是从声明开始到文件结束任何位置
2）局部变量：声明在 函数中 的变量就是局部变量（函数的参数相当于声明在函数中的变量） 

函数调用过程（内存）：压栈
当函数调用的时候，系统会自动在内存的栈区间为这个函数开辟一个独立的内存区域，用来保存在函数中声明的变量。
当函数调用结束，这个内存区域回自动释放
"""
# print("========全局变量=========")
# a = 10
# for x in range(5):
#     b = 20
#     print('循环里面', a)
#     print('循环里面', b)
#
# # a,b都是全局变量
#
#
# def func1():
#     print('函数里面', a)
#     print('函数里面', b)
#
#
# print("========局部变量=========")
#
#
# def func2(x=10, y=20):
#     z = 100
#     print('函数内部', x, y, z)
#
#
# func2()
# print('函数外部：', x)  # NameError: name 'x' is not defined

# 3.global和nonlocal
"""
global和nonlocal函数中的关键字，和return一样只能在函数体中使用
1)global - 在函数中声明一个全局变量
global 变量
变量 = 值

2)nonlocal:在局部的局部中去修改局部变量的值
nonlocal 变量
变量 = 值
"""
# a = 111
#
#
# def func3():
#     a = 222  # 局部变量
#     print('函数内部：', a)
#     global b
#     b = 333
#     print("函数内部", b)
#
#
# func3()
# print("函数外部：", a)
# print("函数外部", b)

print("++++++++nolocal+++++++++")


def func1():
    a = 100

    def func2():
        nonlocal a
        a = 500
        print(a)

    func2()
    print(a)


func1()
