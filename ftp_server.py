"""
ftp 文件服务器 ： 服务端
多线程并发  socket
"""

from socket import *
from threading import Thread
import sys,os
from time import sleep

# 全局变量
HOST = "0.0.0.0"
PORT = 8080
ADDR = (HOST,PORT)
ftp = "/home/tarena/FTP/" # 文件库位置

# 将客户端请求功能封装为类
class FTPServer(Thread):
    """
    查看文件列表，下载，上传，退出处理
    """
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    # 发送文件列表
    def do_list(self):
        # 获取文件列表
        files = os.listdir(ftp)
        if not files:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)

        filelist = ""
        for file in files:
            filelist += file+'\n'
        self.connfd.send(filelist.encode())
        # for file in files:
        #     sleep(0.1)
        #     self.connfd.send(file.encode())
        # self.connfd.send(b'##')

    # 下载文件
    def do_get(self,filename):
        try:
            f = open(ftp+filename,'rb')
        except Exception:
            # 打开失败
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        # 发送文件
        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    # 上传文件
    def do_put(self,filename):
        if os.path.exists(ftp+filename):
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        # 接收文件
        f = open(ftp+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return
            elif data == 'L':
                self.do_list()
            elif data[0] == 'D':
                # D filename
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'U':
                # U filename
                filename = data.split(' ')[-1]
                self.do_put(filename)

# 网络搭建
def main():
    # 创建tcp套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    print("Listen the port 8080...")
    while True:
        # 循环等待处理客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = FTPServer(c)
        t.setDaemon(True)  # 分支线程随主线退出
        t.start()

if __name__ == '__main__':
    main()



