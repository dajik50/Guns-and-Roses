"""
block_io.py
非阻塞IO演示
"""

from socket import *
from time import ctime,sleep

# 日志文件
f = open('socket.log','a+')

# tcp套接字
sockfd = socket()
sockfd.bind(('0.0.0.0',8888))
sockfd.listen(3)

# 设置套接字非阻塞
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(2)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    except (BlockingIOError,timeout) as e:
        sleep(3)
        f.write("%s：%s\n"%(ctime(),e))
        f.flush()
