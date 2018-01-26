#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: browser_input.py 
@time: 2018/1/26 9:45 
"""

# 下面的代码实现了模拟提交提交搜索的功能，首先等页面加载完成，然后输入到搜索框文本，点击提交
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\Program Files\chromedriver\chromedriver.exe')
driver.get("https://www.baidu.com")
elem = driver.find_element_by_id("kw")
# 这里需要注意gbk和utf8的问题
elem.send_keys('sohu')
elem.send_keys(Keys.RETURN)
print driver.page_source

