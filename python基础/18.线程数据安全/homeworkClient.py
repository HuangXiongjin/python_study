"""---author==hxj---"""
from socket import *
client = socket()
client.connect(('10.7.181.117', 2323))
while True:
    print("1.文本信息 2.获取图片 3.退出")
    choice = input("客户机：")

    if choice == '1':
        client.send('文本信息'.encode())

    elif choice == '2':
        client.send('获取图片'.encode())
        picture_info = client.recv(1024)
    else:
        client.close()
        re_date = client.recv(1024)



