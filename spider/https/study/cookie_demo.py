#!/usr/bin/env python  
# encoding: utf-8

# cookie的保存
# 1. 使用cookielib方法声明cookie，用于接收cookie
# 2. urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# 3. 通过handler来构建opener


""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: cookie_demo.py 
@time: 2018/1/24 9:33 
"""

import urllib2
import cookielib


def get_cookies_obj():
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('https://www.baidu.com')
    return cookie


# 保存cookie到文件
def get_cookies_file():
    # 设置保存cookies的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    # 声明一个mozillaCookieJar对象实例用来保存Cookie，然后写入文件
    cookie = cookielib.MozillaCookieJar(filename)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    # 此处的open方法同urllib2的urlopen方法，也可以传入request
    response = opener.open('http://www.baidu.com')
    # 保存cookies
    cookie.save(ignore_discard=True, ignore_expires=True)
    return cookie


# 从文件读取cookie
def read_cookie_file():
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib2.Request("http://www.baidu.com")
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(req)
    print response.read()


if __name__ == '__main__':
    # cookies = get_cookies_obj()
    # cookies = get_cookies_file()
    read_cookie_file()
    # for item in cookies:
    #     print 'Name = ' + item.name
    #     print 'Value = ' + item.value
