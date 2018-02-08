#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: jsondemo.py 
@time: 2018/1/25 10:01 
"""
import json
import requests

# json的使用
# 需要我们传JSON格式的数据过去，所以我们可以用 json.dumps() 方法把表单数据序列化。

url = 'http://httpbin.org/post'
payload = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload))
print r.text
