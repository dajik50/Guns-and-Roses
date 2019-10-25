"""
dict 服务端
逻辑处理，数据内容整合
"""

from socket import *
import os ,sys
import signal
from dict_db import Database
from time import sleep

# 全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
# 数据处理对象
db = Database(database='dict')

# 注册处理
def do_register(c,name,passwd):
    # 数据处理成功得到True，否则得到 False/None
    if db.register(name,passwd):
        c.send(b'OK')
    else:
        c.send(b"Fail")

# 登录处理
def do_login(c,name,passwd):
    # 数据处理成功得到True，否则得到 False/None
    if db.login(name,passwd):
        c.send(b'OK')
    else:
        c.send(b"Fail")

# 查询单词
def do_query(c,name,word):
    db.insert_history(name,word) # 插入历史记录
    mean = db.query(word)
    if mean:
        # mean is not None 查到单词
        msg = "%s : %s"%(word,mean)
        c.send(msg.encode())
    else:
        msg = "Not found the word '%s'."%word
        c.send(msg.encode())

# 处理历史记录
def do_hist(c,name):
    data = db.history(name)
    if not data:
        c.send(b'Fail')
        return
    else:
        c.send(b'OK')
    # data-> ((name,word,time),(),())
    for i in data:
        sleep(0.1)
        msg="%s   %-16s    %s"%i
        c.send(msg.encode())
    sleep(0.1)
    c.send(b'##')

# 客户端处理函数
def request(c):
    db.create_cur() # 生成游标
    while True:
        data = c.recv(1024).decode()
        tmp = data.split(' ') # 解析请求
        if not data or tmp[0] == 'E':
            return
        elif tmp[0] == 'R':
            # [R,name,passwd]
            do_register(c,tmp[1],tmp[2])
        elif tmp[0] == 'L':
            # [L,name,passwd]
            do_login(c,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            # [Q,name,word]
            do_query(c,tmp[1],tmp[2])
        elif tmp[0] == 'H':
            # [H,name]
            do_hist(c,tmp[1])

# 搭建网络
def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(3)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 循环等待客户端连接
    print('Listen the port 8000')
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        pid = os.fork()
        if pid == 0:
            s.close()
            request(c) # 具体处理客户端请求
            os._exit(0)
        else:
            c.close()

if __name__ == '__main__':
    main()




