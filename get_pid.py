import os
pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child PID:",os.getpid())
    print("Get parent PID",os.getppid())
else:
    print("Get child PID:",pid)
    print("Parent PID",os.getpid())