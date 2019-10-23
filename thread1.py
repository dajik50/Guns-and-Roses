"""
thread1.py  线程创建
步骤： 1. 封装线程函数
      2. 创建线程对象
      3. 启动线程
      4. 回收线程
"""

import threading
from time import sleep
import os

a = 1

# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放:我和我的祖国")
    global a
    print("a = ",a)
    a = 10000

# 创建线程对象
t = threading.Thread(target=music)
t.start() # 启动线程

for i in range(2):
    sleep(4)
    print(os.getpid(),"播放：五星红旗")

t.join() # 回收线程

print("a:",a)









