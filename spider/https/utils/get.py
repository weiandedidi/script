#!/usr/bin/python
# -*- coding: utf-8 -*-
# get 方法
# 引入正则表达式
import re
import urllib2

# values = {}
# values['username'] = "1016903103@qq.com"
# values['password'] = "XXXX"
# data = urllib.urlencode(values)
# url = "https://www.che168.com/Handler/ScriptCarList_V1.ashx?needData=1"
url = "https://www.baidu.com"
geturl = url
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

request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)

# 转码
context = re.search('charset=\S*', response.headers['Content-Type'])
charset = context.group(0)
charset = charset.replace("charset=", '')

# 转码就行
print response.read().decode(charset).encode("utf-8")
