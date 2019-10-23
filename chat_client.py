"""
chat room 客户端
发送请求，展示结果
"""

import os
import sys
from socket import *

# 服务器地址
ADDR = ('127.0.0.1', 8888)


# 进入聊天
def login(s):
    while True:
        name = input("输入用户名:")
        msg = 'L ' + name
        s.sendto(msg.encode(), ADDR)  # 发送请求
        # 接收结果
        data, addr = s.recvfrom(128)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            return name
        else:
            print(data.decode())


def send_msg(s, name):
    while True:
        try:
            text = input("发言:")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s" % (name, text)
        s.sendto(msg.encode(), ADDR)


def recv_msg(s):
    while True:
        try:
            data, addr = s.recvfrom(4096)
        except KeyboardInterrupt:
            sys.exit()
        # 从服务器接收到退出指令
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode() + '发言：', end='')


# 启动函数
def main():
    s = socket(AF_INET, SOCK_DGRAM)
    name = login(s)  # 登录

    # 创建新的进程
    pid = os.fork()
    if pid < 0:
        sys.exit("Error")
    elif pid == 0:
        send_msg(s, name)  # 子进程发消息
    else:
        recv_msg(s)  # 收消息


if __name__ == '__main__':
    main()
