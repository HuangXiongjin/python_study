"""---author==hxj---"""
import requests
# python中有一个第三方库叫“request"中提供了所有和http请求相关的函数
# 1.get请求
"""
get(url, params=None) --发送请求获取服务器返回的响应
url --  请求地址，字符串
params -- 请求参数，字典
"""

"""
# 方法一：
url = 'http://www.apiopen.top/satinapi'
params = {'type': 1, 'page': 2}
response = requests.post(url, params)
response = requests.get(url, params)
print(response)

# 方法二：
url = 'http://www.apiopen.top/satinapi?type=1&page=2'
response = requests.get(url)
print(response)
"""

# 2.获取请求结果
# 1)响应头
# {'Server': 'nginx', 'Data': }
# print(response.headers)


# 2) 响应体(数据)
# a.获取二进制对应的原数据（数据本身是图片，压缩文件，视频等文件数据）
# content = response.connet
# print(content)
nums = input("number:")
print("长度是：{}".format(len(nums)))
print("逆序打印为:", end='')
for x in nums[-1::-1]:
    print(x, end='')
