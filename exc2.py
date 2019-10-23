"""
 使用进程池拷贝一个目录及目录中所有内容,实时显示拷贝的百分比
 * 目录中的内容均为普通文件
 * 进程池中执行的每个进程事件拷贝一个文件
"""

from multiprocessing import Pool, Queue
import os

q = Queue()  # 消息队列


# 复制文件
def copy_file(file, old_folder, new_folder):
    fr = open(old_folder + '/' + file, 'rb')
    fw = open(new_folder + '/' + file, 'wb')
    # 开始拷贝
    while True:
        data = fr.read(1024 * 1024)
        if not data:
            break
        n = fw.write(data)  # 返回写入多少字节
        q.put(n)  # 放入消息队列
    fr.close()
    fw.close()


def main():
    base_path = "/home/tarena/"  # 拷贝这个基准目录下的目录
    dir = input("输入你要拷贝的目录:")
    old_folder = base_path + dir  # 待拷贝目录

    # 目标位置
    new_folder = old_folder + '-备份'
    os.mkdir(new_folder)

    all_file = os.listdir(old_folder)  # 获取文件列表

    # 计算目录大小
    totle_size = 0
    for file in all_file:
        totle_size += os.path.getsize(old_folder + '/' + file)

    # 创建进程池
    pool = Pool()
    for file in all_file:
        # 每个copy_file复制一个文件
        pool.apply_async(copy_file, args=(file, old_folder, new_folder))
    pool.close()

    print("目录大小:%.2fM" % (totle_size / 1024 / 1024))
    copy_size = 0
    while True:
        copy_size += q.get()
        print("拷贝了%.1f%%" % (copy_size / totle_size * 100))
        if copy_size >= totle_size:
            break

    pool.join()


main()
