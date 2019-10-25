import getpass
import hashlib

# 隐藏密码输入
passwd = getpass.getpass("PW:")

print("密码：",passwd)

# 加密处理
hash = hashlib.md5(b'salt')  # 加盐处理
hash.update(passwd.encode())
passwd = hash.hexdigest()
print("加密后的内容：",passwd)
