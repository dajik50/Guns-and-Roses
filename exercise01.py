from socket import *

# 创建tcp套接字
sockfd = socket()  # 默认参数
# 链接服务端
server_addr = ('176.209.104.60', 11235)
sockfd.connect(server_addr)
with open('test.txt','rb+')as f:
    data=f.readline()
for i in data:
    # 发消息

    if not data:
        break
    sockfd.send(data)  # 转换为字节串

    msg = sockfd.recv(1024)
    print('服务器：', data)  # 打印接收内容

    # 关闭
sockfd.close()

