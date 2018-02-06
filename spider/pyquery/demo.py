#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: demo.py 
@time: 2018/1/29 11:07 
"""
# pyquery的demo练习，类似jquery
from pyquery import PyQuery as pq
doc = pq(filename='hello.html')
print type(doc)
print doc.html()
print '==========================================================='
li = doc('li')
print type(li)
print li.text()
