"""__author__ = 余婷"""
import json
"""
1.打开文件  -   读/写文件   -   关闭文件
1) 文件对象 = open(文件路径, 读写方式, encoding=编码方式)

'r'  -  只读;读到的内容是字符串
'rb'/'br'   -  只读;读到的内容是二进制

'w'  -  只写; 将字符串写入文件; 会清空原文件
'wb'/'bw'   -  只写; 将二进制写入文件; 会清空原文件
'a'  -   只写; 将字符串写入文件; 不会清空原文件
'ab'/'ba'  -  只写; 将二进制写入文件; 不会清空原文件

with open(文件路径, 读写方式, encoding=编码方式) as 文件对象:
    文件域

2) 文件读写
文件对象.read()
文件对象.readline()

文件对象.write()

3) 关闭文件
文件对象.close()

2.数据持久化
1)需要持久化的数据保存在本地文件中
2)需要数据的时候从文件中读数据(而不是在程序中赋默认值)
3)数据发生改变后需要更新文件


3.json数据 - 是一种数据格式
1)格式: 有且只有一个数据; 这个数据格式是json支持的类型对应的格式

2)类型
数字： 199， 9.23， -128， 3e4
字符串："abc"，"123"，"abc\n123"， "\u4e00"
布尔：true， false
数组：[199, "abc", false]
字典：{"a": 100, "b":"name", "c": [1, 2]}
空值：null

3)json转python
json.loads(字符串)   -  json转python; 字符串的内容是json数据
json.load(文件对象)  -  将文件中的内容转换成python；文件中的内容必须是json

4)python转json
json.dumps(数据)   -  python转json; 数据只能是int、float、bool、str、list、tuple、dict、None
                     结果是内容是json的字符串
json.dump(数据, 文件对象)   -  将python中的数据以json格式写入文件
"""
