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

url = 'https://note.wiz.cn/as/user/login?clientType=web&clientVersion=3.0.0&apiVersion=10&lang=zh-cn'
data = {'userId': 'weiandedidi@163.com', 'password': 'maqidi4915338'}
headers = {'User-agent': 'Mozilla/5.0',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Connection': 'keep-alive',
           'language': 'zh-CN,zh;q=0.9,en;q=0.8',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
# 超时时间
timeout = 1
# timeout = 0.001

result = requests.post(url, data, headers=headers, timeout=timeout)
print result.cookies
print result.text
