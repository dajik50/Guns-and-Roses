import pymysql

# 链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='STU',
                     charset='utf8')
# 生成游标对象(操作数据库，执行sql语句)
cur = db.cursor()
# 执行各种多数据库的读写操作








# sql =  'select * from STU.class_1'
# a = cur.execute(sql)
# for i in cur.fetchall():
#     print(i)
# print(a)#五条数据
# 关闭游标和数据库链接
cur.close()
db.close()
