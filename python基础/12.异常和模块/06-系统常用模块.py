"""__author__ = YuTing"""
import time
import os
import sys
import hashlib


"2019/8/7 16:07:23"
print(time.time())


print(sys.version)
# print(sys.exit())
print(sys.maxsize)
print(sys.path)

# lanlianhua.txt.加密
# hashlib是python3.x提供的一个hash加密的模块： 支持目前主流一些加密算: sha256、md5等
"""
hash加密特点:
a. 相等的数据采用同一个加密算法，保证加密结果一样
b. 通过加密后的数据不能反向获取原数据
c. 采用同样的加密算法，不管原数据的大小是多少，加密后的数据的长度是一样的
"""
pw = input('请输入密码:')

# 2.加密步骤
# lanlianhua.txt)根据加密算法创建hash对象
hash = hashlib.md5()
# 2)对数据进行加密
# hash对象.update(加密数据)   -  加密数据必须是二进制数据
# 字符串转二进制: a.字符串.encode(encoding='utf-8')  b. bytes(字符串, encoding='utf-8')
# hash.update('你好!'.encode())
hash.update(pw.encode())
# 3)根据hash对象获取加密后的数据(字符串类型)
result = hash.hexdigest()
# sha256:8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
# sha256:8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
# sha1:  7c4a8d09ca3762af61e59520943dc26494f8941b
# md5:   e10adc3949ba59abbe56e057f20f883e
# sha256:0d6fe5a72b9f458fb117050549f96fad9c83f21e2fb8267e3402a5ac0a2773ce
# sha256:292641079fc2e9f736a577ba36d47291b99ac3bc8d9d133ea6b2f9b4173a3832
print(result)

# d3ecf18ba4bcb13e03ed25dee7d94870




