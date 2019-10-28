"""
httpserver 主要功能程序 v3.0

获取http请求
解析http请求
将请求发送给WebFrame
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端(浏览器)
"""
from socket import *
from config import *
from threading import Thread
import re
import json

# 用于和webframe通信
def connect_frame(env):
    """
    将请求发送给WebFrame
    从WebFrame接收反馈数据
    """
    s = socket()
    try:
        s.connect((frame_ip, frame_port))
    except:
        print("连接不到webframe")
        return
    # 将请求转换为json发送
    data = json.dumps(env)
    s.send(data.encode())
    # 从webframe接收数据（json）
    data = s.recv(1024 * 1024 * 10).decode()
    if data:
        return json.loads(data)

# 封装http基本功能
class HTTPServer:
    def __init__(self):
        self.address = (HOST, PORT)
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR, DEBUG)

    # 绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.host = self.address[0]
        self.port = self.address[1]

    # 启动服务 (多线程并发)
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %s" % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print("Connect from", addr)
            client = Thread(target=self.handle,
                            args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 处理客户端请求函数
    def handle(self, connfd):
        # 接收请求
        request = connfd.recv(4096).decode()
        pattern = r"(?P<method>[A-Z]+)\s+(?P<info>/\S*)"
        try:
            env = re.match(pattern, request).groupdict()
        except:
            connfd.close()
            return
        else:
            # response -> {status:200,data:xxxx}
            data = connect_frame(env)
            if data:
                self.response(connfd, data)

    # 给浏览器发送http响应
    def response(self, connfd, data):
        # data->{'status':'200','data':'xxxxx'}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += '\r\n'
            responseBody = data['data']
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())


if __name__ == '__main__':
    httpd = HTTPServer()
    httpd.serve_forever()  # 启动服务
