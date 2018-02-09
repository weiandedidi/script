#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: lock_demo.py 
@time: 2018/2/8 14:53 
"""

# 输出的时候加锁，其他进程等待
# 加锁后打印功能不会有争抢方式出现

from multiprocessing import Process, Lock
import time


class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
            self.lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()
