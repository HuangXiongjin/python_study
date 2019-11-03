"""---author==hxj---"""
from socket import *

client = socket()
client.connect(('10.7.181.117', 1313))
while True:
    re_data = client.recv(1024)
    with open('files/new3.jpg', 'ab') as f:
        f.write(re_data)

    if len(re_data) < 1024:
        break


