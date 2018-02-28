#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: beidakouqiang.py 
@time: 2018/2/28 16:44 
"""

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
# 浏览器驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dscp = DesiredCapabilities.PHANTOMJS.copy()
dscp[
    'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
dscp[
    'phantomjs.page.settings.Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
dscp['phantomjs.page.settings.Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
dscp['phantomjs.page.settings.Connection'] = 'keep-alive'
dscp['phantomjs.page.settings.Host'] = 'open.zwjk.com'

service_args = []
service_args.append('--load-images=no')  # 关闭图片加载
service_args.append('--disk-cache=yes')  # 开启缓存
service_args.append('--ignore-ssl-errors=true')  # 忽略https错误
driver = webdriver.PhantomJS(desired_capabilities=dscp, service_args=service_args)


def parse_wap(url):
    driver.get(url)
    # driver.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'rbk-navigate-right'))
        )
        html = driver.page_source
    finally:
        driver.close()
    print html


if __name__ == '__main__':
    url = 'https://open.zwjk.com/appointment/zjyyAAA?phID=16'
    parse_wap(url)
