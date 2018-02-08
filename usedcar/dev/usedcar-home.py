#!/usr/bin/python
# encoding: utf-8
"""
@version: v1.0
@author: qidima
@license: Apache Licence
@contact: weiandedidi@qq.com
@site:
@software: PyCharm
@file: usedcar-home.py
@time: 2018/2/5 16:57
"""
# 配置
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import sys
sys.path.append(r'D:\work\script')
from mysql.utils.mysqlutil import *

url_base = 'https://app.che168.com/czy/web/v152/store/index.html?dealerId='
dscp = DesiredCapabilities.PHANTOMJS.copy()
dscp[
    'phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
dscp[
    'phantomjs.page.settings.Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
dscp['phantomjs.page.settings.Accept-Language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
dscp['phantomjs.page.settings.Connection'] = 'keep-alive'
dscp['phantomjs.page.settings.Host'] = 'app.che168.com'
service_args = []
service_args.append('--load-images=no')  # 关闭图片加载
service_args.append('--disk-cache=yes')  # 开启缓存
service_args.append('--ignore-ssl-errors=true')  # 忽略https错误

# 创建mysql连接
db = Mysql()
driver = webdriver.PhantomJS(desired_capabilities=dscp, service_args=service_args)


# 二手车之家的网站数据

# 解析网站
def parse_site(dealerId):
    url = url_base + str(dealerId)
    driver.get(url)
    site_id = dealerId
    name = ''
    type_info = ''
    sold_num = ''
    sell_num = ''
    phone = ''
    source_id = 1
    address = ''
    html = driver.page_source.decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'lxml')
    name_parent = soup.find_all('div', class_='company-list')
    if len(name_parent) < 1:
        return None
    temps = soup.find('div', class_='company-list')
    if None != temps.find('a'):
        name = temps.find('a').text
    if None != temps.find('mark'):
        type_info = temps.find('mark').text

    tags = soup.find_all('p', class_='info-num-line1')
    sold_num = tags[0].text
    sell_num = tags[1].text
    div_phone = soup.find(id='phone1')
    if None != div_phone:
        phone = div_phone.text
    # 地址
    ul_address = soup.find('ul', {'class': 'list-base gs-info'})
    if None != ul_address:
        comments = ul_address.find_all(text=lambda text: isinstance(text, Comment))
        tag_addr = BeautifulSoup(comments[0], 'lxml')
        div_addr = tag_addr.find('div', {'class': 'right-text fn-right wid100 mt20'})
        address_temp = div_addr.find('span')
        if None != address_temp:
            address = address_temp.text
            # 解决错误乱码
            address = address.encode('gbk', 'ignore')
    dealer = (name, site_id, type_info, sold_num, sell_num, phone, address, source_id, url)
    return dealer


# 插入收据库
def batch_insert(sql, list):
    """
    输入sql和list[tuple]
    :param sql:
    :param list: [tuple1,tuple2]
    :return:
    """
    count = db.insertOne(sql, list)
    return count


def insert_one(sql, params):
    """

    :param sql:
    :param params: tuple()
    :return: 返回插入id
    """
    id = db.insertOne(sql, params)
    print id
    return id


if __name__ == '__main__':
    sql = 'insert into sync_dealer_info(name, site_id, type_info, sold_num, sell_num, phone, address, source_id, url)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    for i in range(304675, 330000, 1):
        dealerId = i
        try:
            dealer = parse_site(dealerId)
            if None == dealer:
                continue
            id = insert_one(sql, dealer)
        except UnicodeEncodeError, e:
            print e.message
        except pymysql.Error, e:
            print e.message
        finally:
            pass
    print '==============================================finished================================================='
    driver.quit()
