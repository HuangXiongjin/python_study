"""---author==hxj---"""
from socket import *

server = socket()
server.bind(('10.7.181.117', 1313))
server.listen(512)
while True:
    print("开始监听。。")
    connect, address = server.accept()
    with open('files/hat.png', 'rb') as f:
        connect.send(f.read())
    connect.close()



