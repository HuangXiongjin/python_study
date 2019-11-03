"""---author==hxj---"""
# 1.对象方法
"""
类中的方法分为：对象方法；类方法；静态方法

1）对象方法：
a.怎么声明：直接声明在类中的函数就是对象方法
b.特点：自带self参数;用对象调用对象方法的时候self不用传参；系统会自动将当前对象传给self。
  self可以做到谁调用就指向谁，只是一种形式。
c.怎么调用：以“对象.方法（）”的形式调用，通过对象来调用方法
"""


class Person:
    def eat(self, food='米饭'):
        print(self)  # <__main__.Person object at 0x00000247FBB42F60>
        print("人在吃饭！")
        print("人在吃{}！".format(food))


p1 = Person()
print(p1)  # <__main__.Person object at 0x00000247FBB42F60> p1调用Person，self就指向了p1
# p1.eat()
p1.eat()
