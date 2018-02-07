#!/usr/bin/python 
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: thread_demo1.py 
@time: 2018/2/7 15:52 
"""

# Python中使用线程有两种方式：函数或者用类继承线程对象。
# 函数方式
# function – 线程函数。
# args – 传递给线程函数的参数,他必须是个tuple类型。
# kwargs – 可选参数。
import time

# 为线程定义一个函数
import thread


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print '%s:%s' % (threadName, time.ctime(time.time()))


# 创建两个线程
# 执行先后顺序不一定
try:
    thread.start_new_thread(print_time, ('thread-1', 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

# 保证主线程一直运行，死循环
while 1:
    pass

print "Main Finished"
