#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: daemon_demo.py 
@time: 2018/2/9 15:23 
"""

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


# 主进程等待其他进程完成后进行
if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        # 守护线程 true就是主进程结束就结束  false就不结束
        p.daemon = True
        p.start()
        # p.join()

    print 'Main process Ended!'
