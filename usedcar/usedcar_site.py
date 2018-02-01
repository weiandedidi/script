#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: usedcar_site.py 
@time: 2018/1/29 17:50 
"""
# 爬取二手车之家wap网站
# 引用 selenium 、bs4 、phantomjs
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import DesiredCapabilities


class seleniumTest(unittest.TestCase):
    def setUp(self):
        pass

    def testEle(self):
        # phantomjs_path = 'D:\Program Files\phantomjs\bin\phantomjs.exe'
        phantomjs_path = '/usr/local/bin/phantomjs'
        # 伪装header
        dscp = DesiredCapabilities.PHANTOMJS.copy()
        dscp[
            'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
        dscp[
            'phantomjs.page.settings.Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        dscp['phantomjs.page.settings.Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
        dscp['phantomjs.page.settings.Connection'] = 'keep-alive'
        dscp['phantomjs.page.settings.Host'] = 'app.che168.com'

        # 驱动
        driver = webdriver.PhantomJS(desired_capabilities=dscp)
        dealerId = 263568
        url = 'https://app.che168.com/czy/web/v152/store/index.html?dealerId=' + str(dealerId)
        # https没有证书的检查
        # 点击元素，获取数据
        driver.get(url)
        # ele = driver.find_element_by_css_selector('span[data-index="4"]')
        ele = driver.find_element_by_id('template_store')
        # 解析html
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # print driver.page_source

    def tearDown(self):
        print 'down'


if __name__ == "__main__":
    unittest.main()
