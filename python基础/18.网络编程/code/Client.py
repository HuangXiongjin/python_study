"""---author==hxj---"""
from socket import socket

client = socket()
client.connect(('10.7.181.117', 3232))
while True:
    message = input('客户端1:')
    client.send(message.encode())

    re_data = client.recv(1024)
    print("接收：", re_data.decode(encoding='utf-8'))

# connect1.close()




