"""---author==hxj---"""

# lanlianhua.txt.什么是模块
"""
python中一个py文件就是一个模块
"""
# 2.怎么一个模块中使用另外一个模块中的内容
"""
如果要在一个模块中去使用另外一个模块中的内容，必须先导入模块
lanlianhua.txt）语法:
a.import 模块名   -  导入指定模块，导入后可以在当前模块中使用模块中所有的全局变量，
                  以'模块名.全局变量名'的方式去使用
                  
b.from 模块名 import 变量名1,变量名2,...   - 导入指定模块，导入后只能使用import后面指定的变量,
                                        导入后指定的全局变量在当前模块中直接使用，不用在前面加'模块名.'
                                        
c.from 模块名 import *   -  导入指定模块，导入后可以在当前模块中使用模块中所有的全局变量;
                         导入后全局变量直接使用，不用加'模块名.'
                         
d.import 模块名 as 新模块名   -  导入后采用新模块名去使用模块中的内容
e.from 模块名 import 变量名1 as 新变量名1, 变量名2 as 新变量名2,...
"""
# 导入方式一:
# import test
# print(test.test_a, test.test_str1)
# test.func1()

# 导入方式二:
# from test import test_a, func1
# print(test_a)
# func1()
# # print(test_str1)   # NameError: name 'test_str1' is not defined

# 导入方式三:
# from test import *
# print(test_a, test_str1)
# func1()

# 模块重命名:
# import fileManager as FM
# FM.write_file(900)
# FM.json_read()

# import time as TIME
# time = 10
# print(TIME.sleep(lanlianhua.txt), time)

# from test import a as ta
# a = 100
# print(a, ta)

# 3.导入模块的原理
"""
当执行导入模块的代码的时候，会直接执行被导入的模块中所有的代码

lanlianhua.txt)重复导入问题
import在导入模块的时候会自动检测这个模块之前是否已经导入过,来避免一个模块的重复导入

2)阻止模块中的内容被其他模块导入
将不需要被其他模块执行的语句写入"if __name__ == '__main__':"对应的if语句中
"""


