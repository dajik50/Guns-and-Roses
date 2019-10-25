#!/usr/bin/env python3
# coding=utf-8

from socket import *
import sys
import getpass


def main():
    if len(sys.argv) < 3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST, PORT)

    s = socket()
    s.connect(ADDR)

    while True:
        print('''\n
            ===========Welcome=========
            --1.注册    2.登录    3.退出--
            ===========================
            ''')
        try:
            cmd = int(input("输入选项>>"))
        except Exception:
            print("输入命令错误")
            continue

        if cmd not in [1, 2, 3]:
            print("对不起，没有该命令")
            sys.stdin.flush()  # 清除输入
            continue
        elif cmd == 1:
            name = do_register(s)
            if name != 1:
                print("注册成功,直接登录！")
                login(s, name)
            else:
                print("注册失败！")
        elif cmd == 2:
            name = do_login(s)
            if name != 1:
                print("登录成功！")
                login(s, name)
            else:
                print("登录失败！")
        elif cmd == 3:
            s.send(b"E")
            sys.exit("谢谢使用")


def do_register(s):
    while True:
        name = input("用户名:")
        passwd = getpass.getpass("密 码:")
        passwd1 = getpass.getpass("确认密码:")

        if (' ' in name) or (' ' in passwd):
            print("用户名密码不允许空格")
            continue
        if passwd != passwd1:
            print("两次密码不一致")
            continue

        msg = "R {} {}".format(name, passwd)
        # 发送请求
        s.send(msg.encode())
        # 接收回复
        data = s.recv(128).decode()

        if data == "OK":
            return name
        elif data == 'EXISTS':
            print("该用户已存在")
            return 1
        else:
            return 1


def do_login(s):
    name = input("用户名:")
    passwd = getpass.getpass("密 码:")
    msg = "L {} {}".format(name, passwd)
    s.send(msg.encode())
    data = s.recv(128).decode()

    if data == 'OK':
        return name
    else:
        print(data)
        return 1


def login(s, name):
    while True:
        print('''\n
            ===========查询界面============
            1.查词     2.历史记录   3.注销
            =============================
            ''')
        try:
            cmd = int(input("输入选项>>"))
        except Exception:
            print("命令错误")
            continue
        if cmd not in [1, 2, 3]:
            print("对不起，没有该命令")
            sys.stdin.flush()  # 清除输入
            continue
        elif cmd == 1:
            do_query(s, name)
        elif cmd == 2:
            do_history(s, name)
        elif cmd == 3:
            return


def do_query(s, name):
    while True:
        word = input("单词:")
        if word == "##":
            break
        msg = "Q {} {}".format(name, word)
        s.send(msg.encode())
        data = s.recv(128).decode()
        if data == 'OK':
            data = s.recv(2048).decode()
            print(data)
        else:
            print(data)


def do_history(s, name):
    msg = "H {}".format(name)
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            data = s.recv(1024).decode()
            if data == "##":
                break
            print(data)
    else:
        print(data)


if __name__ == "__main__":
    main()
