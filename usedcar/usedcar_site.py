#!/usr/bin/python
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

from bs4 import BeautifulSoup, Comment
from selenium import webdriver
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
        driver.get(url)
        # 点击元素，获取数据
        # ele = driver.find_element_by_css_selector('span[data-index="4"]')
        # ele = driver.find_element_by_id('template_store')
        # 解析html
        # 显示等待
        driver.implicitly_wait(10)
        try:
            # print driver.page_source
            soup = BeautifulSoup(driver.page_source, 'lxml')
            tags = soup.find_all('p', class_='info-num-line1')
            # 车源已售，在售
            # for tag in tags:
            #     print tag.text
            sold = tags[0].text
            sell = tags[1].text
            print sold
            print sell
            # 商铺名
            # name_parent = soup.find_all('div', class_='company-list')
            # temps = soup.find('div', class_='company-list')
            # name = temps.find('a').text
            # print name
            # 地址
            ul_address = soup.find('ul', {'class': 'list-base gs-info'})
            # 可遍历字符串
            comments = ul_address.find_all(text=lambda text: isinstance(text, Comment))
            tag_addr = BeautifulSoup(comments[0], 'lxml')
            div_addr = tag_addr.find('div', {'class': 'right-text fn-right wid100 mt20'})
            address = div_addr.find('span')
            print address.string

            div_phone = soup.find(id='phone1')
            print div_phone.text



        finally:
            driver.quit()


def tearDown(self):
    print 'down'


if __name__ == "__main__":
    unittest.main()
