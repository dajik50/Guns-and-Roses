"""
dict 数据端
数据库操作，提供各种服务端需要的数据
"""
import pymysql
import hashlib

# 盐变量
SALT = b"*#06#"

# 加密函数
def md5_passwd(passwd):
    # 加密处理
    hash = hashlib.md5(SALT)  # 加盐处理
    hash.update(passwd.encode())
    return hash.hexdigest()

class Database:
    def __init__(self,host='localhost',
                 port=3306,
                 user='root',
                 password='123456',
                 database=None,
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset=charset
        # 连接数据库
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             password=self.password,
                             database=self.database,
                             charset=self.charset)


    # 生成游标对象 (操作数据库，执行sql语句)
    def create_cur(self):
        self.cur = self.db.cursor()

    def close(self):
        # 关闭游标和数据库连接
        if self.cur:
            self.cur.close()
        self.db.close()

    # 注册处理
    def register(self,name,passwd):
        # 转换密码
        passwd = md5_passwd(passwd)

        # 插入数据库
        sql="insert into user (name,passwd) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
        except Exception:
            self.db.rollback()
            return False
        else:
            return True

    # 处理登录
    def login(self,name,passwd):
        passwd = md5_passwd(passwd)
        # 查找数据库
        sql="select name from user where name=%s and passwd=%s;"
        self.cur.execute(sql,[name,passwd])
        r = self.cur.fetchone()
        if r:
            return True
        else:
            return False

    # 单词查询
    def query(self,word):
        sql="select mean from words where word=%s;"
        self.cur.execute(sql,[word])
        r = self.cur.fetchone()
        if r:
            return r[0]

    # 插入历史记录
    def insert_history(self,name,word):
        sql="insert into hist (name,word) values (%s,%s);"
        try:
            self.cur.execute(sql,[name,word])
            self.db.commit()
        except:
            self.db.rollback()

    def history(self,name):
        sql="select name,word,time from hist " \
            "where name=%s order by time desc limit 10;"
        self.cur.execute(sql,[name])
        return self.cur.fetchall()





