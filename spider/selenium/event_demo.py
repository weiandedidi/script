#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: event_demo.py 
@time: 2018/1/26 10:46 
"""
# 页面交互
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome('D:\Program Files\chromedriver\chromedriver.exe')


# 鼠标点击 Keys.ARROW_DOWN
def arrow_click():
    driver.get("https://www.baidu.com")
    elem = driver.find_element_by_id("kw")
    elem.clear()
    elem.send_keys('sohu')
    elem_sub = driver.find_element_by_id('su')
    elem_sub.send_keys(Keys.ARROW_DOWN)


# 回车 Keys.RETURN
def enter():
    driver.get("https://www.baidu.com")
    elem = driver.find_element_by_id("kw")
    elem.clear()
    elem.send_keys('sina')
    elem.send_keys(Keys.RETURN)


# select元素操作，Select()方法
def form_sub():
    driver.get("file:///D:/work/script/spider/selenium/test.html")
    select = Select(driver.find_element_by_id('sel'))
    select.select_by_value('saab')

if __name__ == '__main__':
    # time.sleep(2)
    # arrow_click()
    # time.sleep(2)
    # enter()
    time.sleep(2)
    form_sub()
    # driver.close()
