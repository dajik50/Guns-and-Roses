"""
httpserver2.0
env:python3.6
io多路复用和http训练
"""

from socket import *
from select import select


# 具体功能实现
def get_data(connfd, info):
    response = "HTTP/1.1 200 OK\r\n"
    response += 'Content-Type: text/html;charset=utf-8\r\n'
    response += '\r\n'
    response += "<h1>敬请期待httpserver3.0</h1>"
    connfd.send(response.encode())


class HTTPServer:
    def __init__(self, host='0.0.0.0', port=8000, dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.address)

    def serve_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d" % self.port)
        self.rlist.append(self.sockfd)

        while True:
            rs, ws, xs = select(self.rlist,
                                self.wlist,
                                self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    self.rlist.append(c)
                else:
                    self.handle(r)

    def handle(self, connfd):
        request = connfd.recv(4096).decode()
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        request_line = request.split('\n')[0]
        info = request_line.split(' ')[1]
        print("Recv request:", info)
        if info == '/' or info[-5:] == ".html":
            # 请求一个网页
            self.get_html(connfd, info)
        else:
            # 处理其他情况
            get_data(connfd, info)

    def get_html(self, connfd, info):
        global response
        if info == '/':
            # 请求主页
            filename = self.dir + "/index.html"
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += 'Content-Type: text/html\r\n'
            response += '\r\n'
            response += "<h1>Sorry...</h1>"
        else:
            response = "HTTP/1.1 200 OK\r\n"
            response += 'Content-Type: text/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            # 将响应内容发送给浏览器
            connfd.send(response.encode())

    # 处理非网页
    def get_data(self, connfd, info):
        response = "HTTP/1.1 200 OK\r\n"
        response += 'Content-Type: text/html;charset=utf-8\r\n'
        response += '\r\n'
        response += "<h1>敬请期待httpserver3.0</h1>"
        connfd.send(response.encode())

if __name__ == '__main__':
    """
    通过HTTPServe类可以快速搭建HTTP服务，展示我的一组网页
    """
    # 用户自己决定
    HOST = '0.0.0.0'
    PORT = 8000
    DIR = "./static"  # 网页存储位置

    # 实例化对象，传入用户指定变量
    httpd = HTTPServer(HOST, PORT, DIR)
    httpd.serve_forever()  # 启动服务
