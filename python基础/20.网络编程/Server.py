"""---author==hxj---"""
from socket import socket

server = socket()
server.bind(('10.7.181.117', 3232))
server.listen(100)
while True:
    connect, address = server.accept()
    print(connect, address)
    while True:
        re_data = connect.recv(1024)
        print("接收：", re_data.decode(encoding='utf-8'))
        message = input('服务器:')
        connect.send(message.encode())
    connect.close()



