#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: post.py 
@time: 2018/1/24 17:49 
"""
# 利用request库进行请求开发

import requests

r = requests.get('http://cuiqingcai.com')
print type(r)
print r.status_code
print r.encoding
# print r.text
print r.cookies
