#!/usr/bin/python
# -*- coding: utf-8 -*-
# post方法

import urllib
import urllib2
import cookielib

filename = 'D:\work\cookies\cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# 设置header
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
# 传输的数据
data = {'userId': 'weiandedidi@163.com', 'password': 'maqidi4915338'}
# 数据urlencode
postdata = urllib.urlencode(data)

loginUrl = 'https://note.wiz.cn/as/user/login?clientType=web&clientVersion=3.0.0&apiVersion=10&lang=zh-cn'
# 使用request请求(url,data,header)
request = urllib2.Request(loginUrl, postdata, headers)
# 使用response获取返回
response = urllib2.urlopen(request)

page = response.read()
print page
