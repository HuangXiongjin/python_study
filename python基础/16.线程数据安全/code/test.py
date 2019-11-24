from re import *


re_str = r'((\d|[0-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[0-9]\d|1\d\d|2[0-4]\d|25[0-5])'
result = fullmatch(re_str, '000.8.21.3')
print(result)

re_str = r'\b[\u4e00-\u9fa5][\u4e00-\u9fa5]\b'
print(search(r'\b\d\d\b', '5画撒86旦法 67 -===双方都建行卡阿斯顿发'))

re_str = r'(\d{3})([a-z]{3})\2'
print(fullmatch(re_str, '234hjshjs'))

re_str = r'\d\d\d$'
print(fullmatch(re_str, '345'))
print(search(re_str, '3457ajhjs789jkals728===sj234=889'))
print(findall(re_str, '789ajhjs789jkals728===sj234=112'))

result = finditer(r'(\d{3})([a-z]{2})', '是234hu士大夫345mmks89h-=数348kl几十块的')
group = []
for x in result:
    group.append(x.group(1))
print(result)
print(group)

message = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
new_message = sub(r'[操肏艹草曹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔', '*', message, flags=IGNORECASE)
print(new_message)