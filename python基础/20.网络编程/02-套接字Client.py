"""---author==hxj---"""
import socket
# 1.创建套接字对象（买电话机）
client1 = socket.socket()

# 2.发送请求（打电话）
client1.connect(('10.7.181.117', 2221))

# 3.发送消息
while True:
    sed_message = input("client:")
    client1.send(sed_message.encode())

    # 4.接收消息
    re_data = client.recv(1024)
    print(re_data.decode(encoding='utf-8'))

# client1.close()

