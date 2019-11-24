"""---author==hxj---"""
from re import fullmatch, search

# 1.什么是正则表达式(regular expression)
"""
正则表达式是处理字符串的工具，通过不同的正则符号来描述字符串的规则
"""
# 2.正则符号(正则表达式的语法)
# 1)普通字符：除了在正则中有特殊功能和特殊意义的符号以外的字符都是普通字符

# fullmatch
"""
fullmatch(正则表达式，字符串) -- 查看字符串和正则表达式是否匹配，如果不匹配结果是None
正则表达式：r'正则语法'
"""
# 1)匹配任意一个字符串有三个字符：分别是'a', 'b', 'c'
re_str = r'abc'
result = fullmatch(re_str, 'abc')
print(result)

# 2）. -- 匹配任意一个字符，一个. 只能匹配一个字符
re_str = r'abc..123'
result = fullmatch(re_str, 'abcwc123')
print(result)

# 3)\w -- 匹配一个数字、字母或者_(在ASCII码表中)
# 一个 \w 只能匹配一个字符
# 匹配以恶搞长度是4的字符串， 第一个字符是数字，字母或者_；后面三个字符是'abc'
re_str = r'\wabc'
result = fullmatch(re_str, '胡abc')
print(result)

# 4) \d -- 匹配任意一个数字字符
# 匹配一个长度是5的字符串，前两个是任意数字，后三个是任意字符
re_str = r'\d\d...'
result = fullmatch(re_str, '34_=*')
print(result)

# 5) \s -- 匹配任意一个空白字符
"""
空白字符包括：空格字符，换行字符，制表符...
"""
result = fullmatch(r'how\sare\syou!', 'how are you!')
print(result)

# 6)\ 大写字母
"""
\D  -- 匹配除了数字字符以外的任意字符（匹配一个非数字字符）
\S -- 匹配一个非空白字符
"""
result = fullmatch(r'\Dabc', '2abc')
print(result)  # None

# 7)[字符集] - 匹配字符集出出现的任意一个字符
"""
注意:一个[]只能匹配一个字符
[abc] -- 匹配abc任意一个字符
[赵谦孙俪] -- 匹配赵谦孙俪中的任意一个字符
"""
# 匹配也该长度是4的字符，第一个字符是1，2，3中的任意一个后面必须是abc
result = fullmatch(r'[123]abc', '3abc')
print(result)  # <re.Match object; span=(0, 4), match='3abc'>
result = fullmatch(r'[123]abc', '4abc')
print(result)  # None

"""
[1-9] -- 匹配1-9中的任意一个字符(字符编码值递增)
[a-z] -- 匹配任意一个字符是小写字母
[A-Z] -- 匹配任意一个字符是大写字母
[a-zA-Z] -- 匹配任意一个字母
[a-zA-Z0-9_] -- 匹配任意一个字母或数字或下划线


"""

# 8）[^字符集] -- 匹配不在字符集中的任意一个字符
"""
例如： [^abc] -- 匹配任意一个不是a, b, c的字符
[^2-8] -- 匹配任意一个不是2到8的字符
[^\u4e00-\u9fa5] -- 匹配任意一个不是中文的字符
"""
result = fullmatch(r'[^2-8]abc', '3abc')
print(result)  # None
result = fullmatch(r'[^2-8]abc', '1abc')
print(result)  # <re.Match object; span=(0, 4), match='1abc'>

print("==============单词边界================")
# 所有的检测符号都不会影响字符串的长度
# 1)\b -- 检查是否都是单词边界
"""
单词边界 -- 能够将两个单词隔开并且不会产生歧义的任意符号。例如：空白字符、标点符号、字符串开头和字符串结尾
匹配规则：先去掉\b对字符串进行匹配，如果匹配成功在检查\b所在的位置是否是单词的边界
"""
re_str = r'abc\b,123'
result = fullmatch(re_str, 'abc,123')
print(result)

re_str = r'\b[\u4e005-\bu9fa][\u4e005-\bu9fa]\b'
print(search(re_str, 'ahfskkfk877===dsf234='))

# 3)$ -- 检查$所在的位时候是否是字符串结尾
