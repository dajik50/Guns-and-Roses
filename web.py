from socket import *

s = socket()
s.bind((('176.209.104.60', 11236)))
s.listen(5)

print('Listen the port 8000...')
c, addr = s.accept()
print('Connect form', addr)
data = c.recv(4096)
print(data.decode())

# 组织http响应
response = """HTTP/1.1 200 OK
Content-Type: text/html;charset=utf-8

为什么我还是乱码？
"""
c.send(response.encode())
