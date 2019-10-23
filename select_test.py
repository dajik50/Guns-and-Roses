"""
select 函数演示
"""

from select import select
from socket import *

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

f = open('test','r')

print("监控IO")
# rs,ws,xs = select([s],[],[],3)
rs,ws,xs = select([s],[],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)




