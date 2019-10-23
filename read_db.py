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
# 执行各种对数据库的读操作
sql = "select * from class_1;"
cur.execute(sql,)  # 执行语句

# while True:
#     name = input("请输入")
#     for i in cur:
#         if name == i[1]:
#             print(i)
# 获取一个查询结果
print(cur.fetchall())

# 关闭游标和数据库链接
cur.close()
db.close()
