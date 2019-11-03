"""---author==hxj---"""
import socket
# 1.什么是socket编程
"""
socket又叫套接字，指的是实现通信的两个端；这两个端又分为服务器套接字和客户端套接字
"""
# 2.服务器套接字
"""
python中提供了一个socket模块支持socket编程
"""
# 1）创建套接字对象（例如买电话机）
"""
socket里面的默认参数：
socket(family=AF_INET, type=SOCK_STREAM)
family -- 这是ip类型; AF_INET --ipv4 ; AF_INET6 -- ipv6
type -- 设置数据传输方式; SOCK_STREAM -- TCP; SOCK_DGRAM -- UDP
"""
server = socket.socket()

# 2）.绑定ip和端口（插电话线）
"""
bind((ip地址,端口号))
ip地址 -- 字符串；服务器程序运行在哪一台计算机上，ip地址就是它的ip地址
端口号 -- 整型；范围是0-65535，器中0-1024是著名端口，有自己特殊的意义不能随便使用
"""
server.bind(('10.7.181.117', 2221))

# 3）.等待连接并且设置同一时间能够接受的请求数量
server.listen(512)

# 4).让服务器一直保持运行状态
while True:
    print("开始监听")
    # 5) 接受请求(接电话)
    # 当程序执行到accept()的时候会停下来，直到有客户端给当前服务器发送请求为止
    connect, address = server.accept()
    print("接收到请求")
    print(connect, address)

    # 6）接收客户端发送的数据(听别人讲电话)
    """
    recv(数据大小) -- 接收数据并且设置一次性能够接收最大的数据
    补充：二进制转字符串
    二进制对象.decode()
    str(二进制对象，encoding='utf-8')
    """
    while True:
        recv_data = connect.recv(1024)
        print("接收", recv_data.decode(encoding='utf-8'))
        # print("接收", str(recv_data, encoding='utf-8'))

        # 7)给客户端发送数据(说话给别人听)
        """
        send(数据) -- 发送的数据类型必须是bytes
        """
        a = input("server:")
        # message = 'HTTP/1.1 200 OK\r\n\n'+a
        connect.send(a.encode())
    connect.close()