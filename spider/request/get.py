#!/usr/bin/python
# encoding: utf-8  
"""
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: get.py 
@time: 2018/1/24 17:52 
"""
# 使用get请求
import requests

r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
headers = {'User-agent': 'Mozilla/5.0', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8', 'Connection': 'keep-alive',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'}
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'}, headers=headers)  # 带参数的GET请求
print(r.status_code)  # 获取返回状态
print(r.url)
print(r.text)  # 打印解码后的返回数据
