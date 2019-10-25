#!/usr/bin/env python3
from __future__ import unicode_literals
# coding=utf-8


from socket import *
import os
import pymysql
import time
import sys
import signal

DICT_TEXT = "./dict.txt"
HOST = '127.0.0.1'
PORT = 11235
ADDR = (HOST, PORT)


def main():
    db = pymysql.connect(host='localhost', user='root', passwd='123456', database='dict', charset='utf8')
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    while True:
        try:
            c, addr = s.accept()
            print("connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        pid = os.fork()
        if pid == 0:
            s.close()
            do_child(c, db)
        else:
            c.close()


def do_child(c, db):
    while True:
        data = c.recv(128).decode()
        print("Request:", data)
        if (not data) or data[0] == 'E':
            c.close()
            sys.exit(0)
        elif data[0] == 'R':
            do_register(c, db, data)
        elif data[0] == "L":
            do_login(c, db, data)
        elif data[0] == 'Q':
            do_query(c, db, data)
        elif data[0] == 'H':
            do_history(c, db, data)


def do_register(c, db, data):
    l = data.split(" ")
    name = l[1]
    passwd = l[2]

    cursor = db.cursor()
    sql = "select * from user where name='%s'" % name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b'EXISTS')
        return
    sql = "insert into  user (name,passwd) values ('%s','%s')" % (name, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send(b'FALL')
        return
    else:
        print("%s注册成功" % name)


def do_login(c, db, data):
    l = data.split(' ')
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where \
    name='%s' and passwd='%s'" % (name, passwd)

    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send('用户名或密码不正确'.encode())
    else:
        c.send(b'OK')


def do_query(c, db, data):
    l = data.split(' ')
    name = l[1]
    word = l[2]
    cursor = db.cursor()

    def insert_history():
        tm = time.ctime()
        sql = "insert into hist (name,word,time)\
             values (%s,%s,%s)" % (name, word, tm)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            return

        try:
            f = open(DICT_TEXT, 'rb')
        except:
            c.send("500 服务端异常".encode())
            return
        while True:
            line = f.readline().decode()
            w = line.split(' ')[0]
            if (not line) or w > word:
                c.send("没找到该单词".encode())
                break
            elif w == word:
                c.send(b'OK')
                time.sleep(0.1)
                c.send(line.encode())
                insert_history()
                break
        f.close()


def do_history(c, db, data):
    name = data.split(' ')[1]
    cursor = db.cursor()

    try:
        sql = "select * from hist \
            where name=%s" % name
        cursor.execute(sql)
        r = cursor.fetchall()
        if not r:
            c.send('没有历史记录'.encode())
            return
        else:
            c.send(b'OK')
    except:
        c.send("数据库查询错误".encode())
        return
    n = 0
    for i in r:
        n += 1
        # 最多显示10条
        if n > 10:
            break
        time.sleep(0.1)
        msg = "%s   %s   %s" % (i[1], i[2], i[3])
        c.send(msg.encode())
    time.sleep(0.1)
    c.send(b'##')


if __name__ == '__main__':
    main()
