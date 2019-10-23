"""
poll_server.py 完成tcp并发
重点代码
"""
from socket import *
from select import *

# 创建套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)


# 创建poll对象
p = poll()

# 建立一个通过文件描述符获取文件对象的字典
# 与register的IO时刻保持一致
fdmap = {s.fileno():s}

# 设置关注IO
p.register(s,POLLIN|POLLERR)

# 循环监控IO发声
while True:
    events = p.poll() # events->[(fileno,event),..]
    # 遍历列表，查看哪个IO就绪，就进行处理
    for fd,event in events:
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from",addr)
            p.register(c,POLLIN|POLLERR) # 添加关注
            fdmap[c.fileno()] = c # 维护字典
        # 判断是否为c的POLLIN发生
        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd) # 取消关注
                fdmap[fd].close()
                del fdmap[fd] #从字典中删除
            else:
                print(data)
                fdmap[fd].send(b'OK')





