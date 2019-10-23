import time,os,signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

def fun01():
    time.sleep(3)
    print('事件1')
def fun02():
    time.sleep(2)
    print('事件2')


pid = os.fork()
if pid < 0:
    print('Error')
elif pid == 0:
    p = os.fork()#创建二级子进程
    if p == 0:
        fun02()#二级子进程做一件
    else:
        os._exit(1)
else:
    os.wait()#等一级子进程退出
    fun01()#父进程做一件