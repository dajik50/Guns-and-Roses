"""
tcp_client.py  tcp客户端流程
重点代码
"""
from socket import *

# 创建tcp套接字
sockfd = socket()  # 默认参数

# 连接服务端
server_addr = ('172.40.91.159',8888)
sockfd.connect(server_addr)

# 发消息
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode()) # 转换为字节串
    # if data == '##':
    #     break
    msg = sockfd.recv(1024)
    print("服务器：",msg.decode()) # 打印接收内容

# 关闭
sockfd.close()



