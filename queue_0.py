"""
queue_0.py 消息队列演示
注意： 多个进程需要使用同一个消息队列
"""

from multiprocessing import Process,Queue
from time import sleep

# 消息队列
q1 = Queue(3)
q2 = Queue(3)

def request():
    print("使用wx登录？")
    q1.put("请求用户名密码") # 写消息队列
    data = q2.get()
    print("获取到信息:",data)

def handle():
    data = q1.get() # 读消息队列
    print("收到请求:",data)
    sleep(3)
    q2.put({'name':'zhang','passwd':'123'})

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()




