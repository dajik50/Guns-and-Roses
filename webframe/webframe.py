"""
模拟网站的后端应用，提供网页或者其他数据

从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""

from socket import *
import json
from setting import *
from multiprocessing import Process
import signal
from urls import urls

# 应用类，将功能封装其中
class Application:
    def __init__(self):
        # 建立套接字
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)
        self.sockfd.bind((frame_ip,frame_port))
        signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    # 多进程并发服务
    def start(self):
        self.sockfd.listen(5)
        print("Running web server on %s"%frame_port)
        while True:
            connfd,addr = self.sockfd.accept()
            p = Process(target=self.handle,args=(connfd,))
            p.daemon = True
            p.start()

    # 完成具体请求
    def handle(self,connfd):
        # 接收请求
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request->{'method':'GET','info':'xxx'}
        # 判定请求类型和请求内容
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                    request['info'][-5:]=='.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])

        elif request['method'] == 'POST':
            pass
        # response->{'status':'200','data':'xxxxx'}
        # 将数据发送给httpserver
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    # 处理网页
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + '/index.html'
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except Exception as e:
            f = open(STATIC_DIR + '/404.html')
            return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}

    # 数据处理
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        return {'status': '404', 'data':'Sorry..'}

if __name__ == '__main__':
    app = Application()
    app.start()


