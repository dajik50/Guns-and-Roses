"""
dict 客户端
发起请求，展示结果
"""

from socket import *
import sys
import getpass

# 服务器地址
ADDR = ('127.0.0.1',8000)

# 生成套接字连接
s = socket()
s.connect(ADDR)

# 注册
def do_register():
    while True:
        name = input("User:")
        passwd = getpass.getpass()
        passwd_ = getpass.getpass("Again:")
        if passwd != passwd_:
            print("两次密码不一致")
            continue
        if (' ' in name) or (' ' in passwd):
            print("用户名密码不能有空格")
            continue

        msg = "R %s %s"%(name,passwd)
        s.send(msg.encode()) # 发送请求
        data = s.recv(128).decode() # 得到反馈
        if data == 'OK':
            print("注册成功")
            # login(name)  # 是否进入二级界面
        else:
            print("注册失败")
        return

# 登录
def do_login():
    name = input("User:")
    passwd = getpass.getpass()

    msg = "L %s %s" % (name, passwd)
    s.send(msg.encode())  # 发送请求
    data = s.recv(128).decode()  # 得到反馈
    if data == 'OK':
        print("登录成功")
        login(name)
    else:
        print("登录失败")
    return

# 登录状态下的界面
def login(name):
    while True:
        print("""
        =============Query=============
         1.查单词   2.历史记录   3.注销
        ===============================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_query(name)
        elif cmd == '2':
            do_hist(name)
        elif cmd == '3':
            return
        else:
            print("请输入正确命令")

# 查单词
def do_query(name):
    while True:
        word = input("Word:")
        if word == '##':
            # 结束查询
            break
        msg = "Q %s %s"%(name,word)
        s.send(msg.encode())
        # 将结果打印
        data = s.recv(2048).decode()
        print(data)

# 历史记录
def do_hist(name):
    msg="H %s"%name
    s.send(msg.encode())
    data = s.recv(128).decode()
    if data == 'OK':
        while True:
            # 循环接收历史记录
            data = s.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("您还没有历史记录哦")

# 连接服务端
def main():
    while True:
        print("""
        ===========Welcome===========
         1. 注册   2. 登录    3. 退出
        =============================
        """)
        cmd = input("输入选项:")
        if cmd == '1':
            do_register()
        elif cmd == '2':
            do_login()
        elif cmd == '3':
            s.send(b'E')
            sys.exit('谢谢使用')
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()