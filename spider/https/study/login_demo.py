#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: login_demo.py 
@time: 2018/1/24 10:06 
"""
# 模拟未知笔记网站登录
import cookielib
import urllib2
import urllib


def login():
    filename = 'wiz_cookies.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    url = 'https://note.wiz.cn/as/user/login?clientType=web&clientVersion=3.0.0&apiVersion=10&lang=zh-cn'
    data = {'userId': 'weiandedidi@163.com', 'password': 'maqidi4915338'}
    postData = urllib.urlencode(data)
    # 设置header
    opener.addheaders = [('User-agent', 'Mozilla/5.0'),
                         ('Accept-Language', 'zh-CN,zh;q=0.9,en;q=0.8'),
                         ('Connection', 'keep-alive'),
                         ('language', 'zh-CN,zh;q=0.9,en;q=0.8'),
                         ('Accept',
                          'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')]
    # 发数据
    result = opener.open(url, postData)
    cookie.save(ignore_discard=True, ignore_expires=True)


# 从文件读取cookie
def read_cookie_file(filename):
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load(filename, ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib2.Request("https://note.wiz.cn/web")
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    login()
    read_cookie_file('wiz_cookies.txt')
