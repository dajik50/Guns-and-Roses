"""
chat room
env: python3.6
socket udp  & fork
"""

import os
from socket import *

# 很多局部空间都使用的变量或者有特定含义的变量可以定义全局
ADDR = ('0.0.0.0', 8888)  # 服务端地址

# 存储用户信息 {name:address}
user = {}


# 处理登录
def do_login(s, name, addr):
    if name in user or '管理' in name:
        s.sendto("该用户存在".encode(), addr)
        return
    s.sendto(b'OK', addr)  # 可以进入聊天室

    # 告知其他人
    msg = "欢迎‘%s’进入聊天室" % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    user[name] = addr  # 字典增加一项


# 转发消息
def do_chat(s, name, text):
    msg = "%s: %s" % (name, text)
    for i in user:
        # 不发送给自己
        if i != name:
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = "‘%s’退出了聊天室" % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    del user[name]  # 删除用户


def request(s):
    """
    循环接收客户端请求，选择不同的功能函数处理
    """
    while True:
        data, addr = s.recvfrom(1024)  # 接收请求
        tmp = data.decode().split(' ', 2)  # 拆分请求
        # 根据不同的请求类型执行不同函数:L C Q
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            do_chat(s, tmp[1], tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 启动函数 启动服务
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)
    # 处理请求函数
    pid = os.fork()
    if pid == 0:
        while True:
            text = input("管理员消息：")
            msg = "C 管理员 " + text
            s.sendto(msg.encode(), ADDR)
    else:
        request(s)


if __name__ == '__main__':
    main()
