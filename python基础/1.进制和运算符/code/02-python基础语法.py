"""---author---hxj"""
# 1.注释
# 1）单行注释：在一行文字前面加#（快捷键：ctrl+/）
# 一行文字
# 2）多行注释：将注释内容写在三个英文双引号或者单引号里面（但是一般使用三个双引号）
"""
多行注释1
多行注释2
...
"""
# 2.语句
# 1）一条语句占一行，语句结束后不用加分号。
# 2）如果一行要显示多行语句，语句之间必须用分号隔开
# 3）如果一条语句很长，需要很多行显示的时候，可以在语句中加\然后在换行（注意：\不能破坏数据）
# num = 10; str1 = 'abc'

# 3.缩进
# 1）python中一样代码的开头不能随便缩进（空格或者制表符）
# 2）python语法要求必须有缩进的位置一定要加缩进

# 4.标识符
# 标识符是用来命名的。一般是给变量命名、函数命名或者类命名
# 标识符规则：所有用来命名的东西，必须是有字母、数字和下划线组成；数字不能开头
# 注意：python2.X以后，标示符中可以出现中文、日语、韩语等符号；但实际不建议使用
胡说 = 234
print(胡说)
# 5.关键字（保留字）
# 关键字就是python中有特殊功能和特殊意义的单词
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
import keyword
print(keyword.kwlist)
"""
# 6.常见的数据类型和数据
"""
1)数字数据：整型（int）    10, 45,35
2)浮点型 float()  12.9, 23.0
3）布尔型（bool） 用只有True和False里昂个值，Ture代表真/肯定，False代表假/否定
2)字符串（str）：'hello'
4）列表(list)，元组(tuple)，集合(set)，字典(dic)，函数(function)等
5）类型转换：类型名（数据）----> 将括号中的数据抓换成指定的类型并返回
"""
# 7.print和input
"""
print函数 --- 输出函数，在控制台打印print括号中内容的结果
input函数 --- 输入函数，获取从控制台输入的内容（输入完回车）,不管输入的是什么，
返回的结果的类型都是字符串类型
input（提示信息）
"""
print('abc')
value = input('请输入年龄：')
print(value)
