"""
select tcp服务
重点代码

思路分析：
   1. 所有的IO使用select监控
   2. 每个IO发生时进行处理，没有发生时即进入监控状态
   3. 每个io不会长期阻塞服务端执行
"""

from socket import *
from select import select

# 创建套接字，作为关注的IO
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

# 将关注的IO放入监控列表
rlist = [s]
wlist = []
xlist = []

# 循环监控IO发生
while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    # for循环逐个取出就绪IO
    for r in rs:
        # 将取出的IO根据不同情况进行处理
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c) # 将c加入监控列表
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r) # 对应套接字不再关注
                r.close()
            else:
                print(data)
                # r.send(b'OK')
                wlist.append(r) # 将这个IO加入写监控

    for w in ws:
        w.send(b'wlist wow')
        wlist.remove(w)






