"""
multiprocessing模块完成
创建两个子进程,分别复制一个文件的上半部分和下半部分
，将他们各自复制到一个新文件里。
"""

from multiprocessing import Process
import os

filename = './yun.jpg'
size = os.path.getsize(filename)

'''
父进程中打开IO操作，如果子进程继承了这个IO对象，
那么父子进程实际使用的是同一个IO
'''
# fr = open(filename,'rb') # 父进程中打开
# print(fr.fileno())

# 复制上半部分
def top():
    fr = open(filename,'rb')
    print(fr.fileno())
    fw = open('top.jpg','wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    print(fr.fileno())
    fw = open('bot.jpg', 'wb')
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)

p2.start()
p1.start()

p1.join()
p2.join()







