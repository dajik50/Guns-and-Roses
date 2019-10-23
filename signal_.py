import time,os,signal
signal.signal(signal.SIGCHLD,signal.SIG_IGN)


pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('Child PID:',os.getpid())
    os._exit(1)
else:
    while True:
        pass