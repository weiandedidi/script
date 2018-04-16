#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: md5_demo.py 
@time: 2018/3/1 11:39 
"""
import md5
import random
import string

# 生成随机字符串
import time

randstr = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(11))
# 13位时间戳
millis = int(round(time.time() * 1000))
print 'noticeStr= ' + randstr
print 'timestamp= ' + str(millis)
executionId = 'process:032742a4-383e-4ce6-af5b-aa8d37485a30'
pageFormKey = '1-7-4'
stepId = 'F_1-7-4'
ucUiFlowId = '98db3dd2-b2d2-11e6-a249-525400644ee2'

strxx = 'executionId=process:032742a4-383e-4ce6-af5b-aa8d37485a30&noticeStr=' + str(randstr)+ '&pageFormKey=1-7-4&stepId=F_1-7-4&timestamp='+ str(millis) +'&ucUiFlowId=98db3dd2-b2d2-11e6-a249-525400644ee2'
m1 = md5.new()
m1.update(strxx.encode(encoding='utf-8'))
print(m1.hexdigest())
