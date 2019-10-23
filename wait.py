import os
from time import sleep

print("=========================")
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process")
else:
    p,status = os.wait()
    print("Parent process")