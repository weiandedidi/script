#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: demo_chrome.py 
@time: 2018/1/26 9:24 
"""

# 使用Selenium打开chrome浏览器
from selenium import webdriver

# 加载chrome浏览器驱动 webdriver.Chrome(chromedriver path)
browser = webdriver.Chrome('D:\Program Files\chromedriver\chromedriver.exe')
# browser = webdriver.Chrome('/Users/qidima/Work/software/chromedriver')
browser.get('http://www.baidu.com/')
