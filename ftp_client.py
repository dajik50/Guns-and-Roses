"""
ftp文件服务： 客户端
"""
from socket import *
import sys
import time

# 服务器地址
ADDR = ('127.0.0.1',8080)

# 客户端功能类
class FTPClient:
    """
    客户端 查看文件库，下载，上传，退出
    """
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b'L') # 发送请求
        # 等待回复
        data = self.sockfd.recv(128).decode() # 回复
        if data == 'OK':
            # 一次接收所有文件名
            data = self.sockfd.recv(4096)
            print(data.decode())
            # while True:
            #     file = self.sockfd.recv(128).decode()
            #     if file == '##':
            #         break
            #     print(file)
        else:
            print(data)

    # 退出
    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit("谢谢使用")

    # 下载
    def do_get(self,filename):
        # 发送请求
        self.sockfd.send(('D '+filename).encode())
        # 等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename,'wb')
            # 循环接收文件
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    # 上传
    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except Exception:
            print("该文件不存在")
            return
        # 获取真正文件名
        filename = filename.split('/')[-1]
        # 发送请求
        self.sockfd.send(('U '+filename).encode())
        # 接收反馈
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b'##')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)

# 网络连接
def main():
    sockfd = socket()
    sockfd.connect(ADDR)

    # 实例化对象
    client = FTPClient(sockfd)

    # 循环发起请求
    while True:
        print("\n========Command===========")
        print("***        list         ***")
        print("***      get file       ***")
        print("***      put file       ***")
        print("***        quit         ***")
        print("============================")

        cmd = input("输入命令:")
        if cmd.strip() == 'list':
            client.do_list()
        elif cmd.strip() == 'quit':
            client.do_quit()
        elif cmd[:3] == 'get':
            filename = cmd.split(' ')[-1]
            client.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.split(' ')[-1]
            client.do_put(filename)
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()







