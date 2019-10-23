"""
epoll_server.py 完成tcp并发
重点代码
"""
from socket import *
from select import *

# 创建套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)


# 创建epoll对象
ep = epoll()

# 建立一个通过文件描述符获取文件对象的字典
# 与register的IO时刻保持一致
fdmap = {s.fileno():s}

# 设置关注IO
ep.register(s,EPOLLIN|EPOLLERR)

# 循环监控IO发声
while True:
    events = ep.poll() # events->[(fileno,event),..]
    print("你有新的IO需要处理哦",events)
    # 遍历列表，查看哪个IO就绪，就进行处理
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            # EPOLLET设置边缘出发
            ep.register(c,EPOLLIN|EPOLLERR|EPOLLET) # 添加关注
            fdmap[c.fileno()] = c # 维护字典
        # 判断是否为c的EPOLLIN发生
        # elif event & EPOLLIN:
        #     data = fdmap[fd].recv(1024).decode()
        #     if not data:
        #         ep.unregister(fd) # 取消关注
        #         fdmap[fd].close()
        #         del fdmap[fd] #从字典中删除
        #     else:
        #         print(data)
        #         fdmap[fd].send(b'OK')





