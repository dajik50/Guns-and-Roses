"""
线程属性说明
"""
from threading import Thread
from time import sleep

def fun():
    print("============")
    sleep(3)
    print("线程属性测试")

t = Thread(target = fun)

t.setDaemon(True) # 主线程退出分支线程也退出

t.start()

print("Name:",t.getName()) # 线程名称
print("is Alive:",t.is_alive()) # 是否在生命中期
print("daemon:",t.isDaemon()) # daemon属性值