"""---author==hxj---"""
import threading
from datetime import datetime
from time import sleep
# 1.线程（thread）
"""
每个进程默认都有一条线程，这个线程叫主线程。其他线程叫子线程。
threading模块中的Thread的对象就是线程对象，当程序中需要子线程就创建Thread类的对象
"""


def download(film_name):
    print("开始下载%s%s" % (film_name, datetime.now()))
    sleep(5)
    print("开始下载%s%s" % (film_name, datetime.now()))


if __name__ == '__main__':
    # download("哪吒之魔童降世")
    # download("扫毒Ⅱ")
    # download("追龙Ⅱ")

    # 1.创建线程对象
    """
    Thread(target=None, args=()) -- 创建并且返回一个子线程对象
    target -- 函数类型(function),在线程启动的时候这个函数会在子线程中进行
    agrs -- 元组，元组中的元素就是target对应的函数在子线程中调用的时候传的实参
    """
    t1 = threading.Thread(target=download, args=("哪吒之魔童降世",))
    t2 = threading.Thread(target=download, args=("扫毒Ⅱ",))
    t3 = threading.Thread(target=download, args=("追龙Ⅱ",))
    # 2.启动线程
    """
    线程对象.start() -- 让线程执行进程中的任务
    target(*args)
    """
    t1.start()
    t2.start()
    t3.start()
