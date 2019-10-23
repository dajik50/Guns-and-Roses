import pymysql
import re

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
# 生成游标对象(操作数据库，执行sql语句)
cur = db.cursor()
f = open('/home/tarena/Alex/dict.txt')
args_list = []
for line in f:
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    args_list.append(tup)
f.close()

sql = "insert into words (word,mean) values (%s,%s);"
try:
    cur.executemany(sql, args_list)
    db.commit()
except:
    db.rollback()

cur.close()
db.close()
