#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: custom.py 
@time: 2018/2/8 14:23 
"""
# deamon
# 守护进程，每个进程都可以单独设置它的属性，
# 如果设置为True，当父进程结束后，子进程会自动被终止。
# 默认是false

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(0.5)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()
        p.join()

    print 'Main process Ended!'
