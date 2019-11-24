"""---author==hxj---"""
from socket import *
from threading import *
import os
from json import *


class DealClientThread(Thread):
    def __init__(self, connection: socket, address):
        super().__init__()
        self.connection = connection
        self.address = address

    def run(self) -> None:
        while True:
            re_date = self.connection.recv(1024)
            message = re_date.decode('utf-8')
            if message == '文本信息':
                self.connection.send("文本".encode())
            elif message == '获取图片':
                picture_info = os.listdir('./my picture')
                self.connection.send(dumps(picture_info).encode())

            else:
                self.connection.close()
                break


def CreatServer():
    server = socket()
    server.bind(('10.7.181.117', 2323))
    server.listen(512)

    while True:
        print("开始监听...")
        connection, address = server.accept()
        t1 = DealClientThread(connection, address)
        t1.start()


if __name__ == '__main__':
    CreatServer()