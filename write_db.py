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
# 执行各种数据库写操作
try:
    #执行增删改等语句
    sql = "delete from class_1 where name='Logic'"
    cur.execute(sql)
except Exception as e:
    db.rollback()
    print(e)

# 关闭游标和数据库链接
cur.close()
db.close()
