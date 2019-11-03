"""---author==hxj---"""
from threading import *
from datetime import datetime
from time import sleep

# 程序结束
"""
线程中的所有任务完成以后线程结束
进程中的所有线程完成以后进程结束
程序出现异常结束的是线程
"""
# 1.声明一个类继承Thread
# 2.实现类中的run方法，这个方法中的代码就是需要在子线程中执行的代码
# 3.需要子线程的时候就创建自己声明的类的对象，并且不需要任何参数


class DownloadThread(Thread):
    def __init__(self, film_name):
        super().__init__()
        self.film_name = film_name

    def run(self) -> None:
        print("开始下载%s%s" % (self.film_name, datetime.now()))
        sleep(5)
        print("开始下载%s%s" % (self.film_name, datetime.now()))


if __name__ == '__main__':
    t1 = DownloadThread("哪吒之魔童降世")
    t2 = DownloadThread("扫毒Ⅱ")
    t3 = DownloadThread("追龙Ⅱ")

    t1.start()
    t2.start()
    t3.start()
