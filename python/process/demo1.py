#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: demo1.py 
@time: 2018/2/8 10:42 
"""

# process进程
# 基本使用
# 在multiprocessing中，每一个进程都用一个Process类来表示。首先看下它的API
#
#
# Process([group [, target [, name [, args [, kwargs]]]]])
# target表示调用对象，你可以传入方法的名字
# args表示被调用对象的位置参数元组，比如target是函数a，他有两个参数m，n，那么args就传入(m, n)即可
# kwargs表示调用对象的字典
# name是别名，相当于给这个进程取一个名字
# group分组，实际上不使用
# process.start()启动
# cpu_count()当前cup核心数量
# active_children()所有运行的进程
import multiprocessing


def process(num):
    print 'Process:', num


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')
