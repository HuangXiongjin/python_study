"""__author__ = YuTing"""

import json

# lanlianhua.txt.文件操作
"""
打开文件  -> 操作文件(读、写)  ->  关闭文件
lanlianhua.txt)打开文件
文件对象 = open(file, mode='r', encoding=None)

'r'('rt')  
'rb'/'br'
'w'('wt')
'wb'
'a'('at')
'ab'


with open(file, mode='r', encoding=None) as 文件对象:
    文件作用域中
    

2)操作文件
文件对象.read()   
文件对象.readline()
文件对象.readlines()

文件对象.write(内容)    -  内容可能是字符串或者二进制(bytes)
"""
with open('files/test.txt', encoding='utf-8') as f:
    print(f.readlines())


with open('files/test.txt', 'w', encoding='utf-8') as f:
    f.write('abcabc')
    # f.writelines(['how\n', 'are\n', 'you\n'])

# 2.数据持久化
"""
lanlianhua.txt) 需要持久化的数据保存在文件中
2) 程序中需要数据的时候去文件中取数据
3) 数据发生改变后需要更新文件中的内容
"""

# 3.json数据
"""
lanlianhua.txt) json格式: a.一个json只有一个数据   b.这个数据是json支持的数据类型的数据
2) json支持的数据类型
数字类型:  100, 2.45, -23, -23.56
字符串:    "abc", "123\nko", "\u4567"
布尔值:    true,false
数组：     [100, "abc", true]
字典:      {"name": "xiaoming", "age": 18}
空值:      null


json.loads(json格式的字符串)
json.dumps(python数据)
"""



