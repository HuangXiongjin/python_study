"""---author==hxj---"""

import time
import sys
import hashlib
pw = input('输入密码：')
hash = hashlib.md5()
hash.update(pw.encode())
result = hash.hexdigest()
print(result)
print(time.time())
print(sys.version)
print(sys.path)
print(sys.maxsize)
