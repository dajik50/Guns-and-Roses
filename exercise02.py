import os
from time import sleep

pid = os.fork()
if pid < 0:
    print("Create prcess failed")
elif pid == 0:
    sleep(3)
    print("The new process")
else:
    sleep(4)
    print("The old process")
print("Fork test over")
