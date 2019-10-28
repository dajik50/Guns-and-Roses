"""
测试httpserver功能
"""
from socket import *
import json

s = socket()
s.bind(('0.0.0.0',8080))
s.listen(3)

while True:
    c,addr = s.accept()
    # data->{'method':'GET','info':'xxx'}
    data = c.recv(1024).decode()
    print(json.loads(data))

    data = {'status':'200','data':'OK'}
    c.send(json.dumps(data).encode())

