#!/usr/bin/python
# -*- coding: utf-8 -*-
# 获取二手车之家的车型库
import urllib
import urllib2
import re

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "https://www.che168.com/Handler/ScriptCarList_V1.ashx?needData=1"
geturl = url + "?" + data
request = urllib2.Request(url)
response = urllib2.urlopen(request)
# 转码
context = re.search('charset=\S*', response.headers['Content-Type'])
charset = context.group(0)
charset = charset.replace("charset=", '')
# 转码就行
print response.read().decode(charset).encode("utf-8")
