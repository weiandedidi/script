#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: login.py 
@time: 2018/1/24 14:44 
"""
# 登录工具类
import cookielib
import urllib2
import urllib


def login(url, headers, data):
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    postData = urllib.urlencode(data)
    # 设置header
    opener.addheaders = headers
    # 登录
    result = opener.open(url, postData)
    return cookie


if __name__ == "__main__":
    url = 'https://note.wiz.cn/as/user/login?clientType=web&clientVersion=3.0.0&apiVersion=10&lang=zh-cn'
    headers = [('User-agent', 'Mozilla/5.0'),
               ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8'),
               ('Connection', 'keep-alive'),
               ('language', 'zh-CN,zh;q=0.9,en;q=0.8'),
               ('Accept',
                'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')]
    data = {'userId': 'weiandedidi@163.com', 'password': 'maqidi4915338'}
    cookies = login(url, headers, data)
    # 继续请求
    req = urllib2.Request("https://note.wiz.cn/web")
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
    response = opener.open(req)
    print response.read()
