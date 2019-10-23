from socket import *
import struct

st = struct.Struct("i16sif")
s = socket(AF_INET, SOCK_DGRAM)
addr = ('176.209.104.60', 11235)
while True:
    print("============================")
    id = int(input("ID:"))
    name = input("NAME:").encode()
    age = int(input("AGE:"))
    score = float(input("SCORE:"))
    # 打包发送
    data = st.pack(id, name, age, score)
    s.sendto(data, addr)
