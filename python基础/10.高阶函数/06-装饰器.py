"""---author==hxj---"""
# 装饰器是python的三大神器之一（迭代器，生成器，装饰器）
"""
1.什么是装饰器：装饰器本质还是一个函数
装饰器的作用：在不修改函数本身的前提下给函数添加功能


"""
# 方式一：给函数添加功能需要修改源代码
# def sum1():
#     start = time.time()
#     print('和', x+y)
#     end = time.time()
#     print()


def password(fn):
    def test(*args, **kwargs):
        # ps = input('请输入密码:')
        # if ps == '321':
        fn(*args, **kwargs)
        print('装饰器')
    return test


@password
def func3():
    print('函数3')


func3()


@password
def func4(x, y):
    print('函数4:', x+y)


func4(10, 20)
