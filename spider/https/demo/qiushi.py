#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: qiushi.py 
@time: 2018/1/24 16:42 
"""
# 糗事百科的爬虫
import urllib2

page = 1
url = 'https://www.qiushibaike.com/hot/page/' + str(page)
# 设置消息头
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
host = 'www.che168.com'
connection = 'keep-alive'
language = 'zh-CN,zh;q=0.9,en;q=0.8'
accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
headers = {'Accept': accept}
headers = {'Accept-Language': language}
headers = {'Connection': connection}
headers = {'Host': host}
headers = {'User-Agent': user_agent}

try:
    request = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
