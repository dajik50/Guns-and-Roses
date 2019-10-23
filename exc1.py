"""
求100000以内质数之和，
将过程封装为函数， 可以使用sum()函数求和
统计函数执行所用时间
"""
from multiprocessing import Process
import time

def timeit(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("%s函数运行时间：%.6f"%(f.__name__,end_time-start_time))
        return res
    return wrapper

# 判断一个数是否为质数
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True

# 求100000以内质数之和 12.944194
@timeit
def prime():
    pr = []
    for i in range(1,100001):
        if isPrime(i):
            pr.append(i)
    print(sum(pr))

# prime()

# 自定义进程类
class Prime(Process):
    def __init__(self,pr,begin,end):
        super().__init__()
        self.pr = pr
        self.begin = begin
        self.end = end
    # 求begin -- end 区间内质数之和
    def run(self):
        for i in range(self.begin,self.end+1):
            if isPrime(i):
                self.pr.append(i)
        print(sum(self.pr))

@timeit
def use_4_process():
    jobs = []
    for i in range(1,100001,25000):
        p = Prime([],i,i+25000)
        jobs.append(p)
        p.start()
    [ps.join() for ps in jobs]

# use_4_process() # 7.430403

@timeit
def use_10_process():
    jobs = []
    for i in range(1,100001,10000):
        p = Prime([],i,i+10000)
        jobs.append(p)
        p.start()
    [ps.join() for ps in jobs]

use_10_process() # 6.820097


