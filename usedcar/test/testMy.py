#!/usr/bin/python
# encoding: utf-8
"""
@version: v1.0
@author: qidima
@license: Apache Licence
@contact: weiandedidi@qq.com
@site:
@software: PyCharm
@file: testMy.py
@time: 2018/2/5 18:01
"""
import unittest
# 创建mysql连接
# 引用自建包的路径的  1. 引入sys  2.sys.path.append(r'project path')  3. from import
import sys
sys.path.append(r'D:\work\script')
from mysql.utils.mysqlutil import *
db = Mysql()


class testUtils(unittest.TestCase):

    def setUp(self):
        pass

    def testSelect(self):
        # pass
        sql = 'select * from user'
        one = db.getAll(sql)
        print one

    def testInsert(self):
        pass

    def testUpdate(self):
        pass

    def testBatchInsert(self):
        pass

    # sql = 'insert into user(name,departId,age)values(%s,%s,%s)'
    # list = []
    # for i in range(1, 50):
    #     temp = ('name' + str(i), 2, i)
    #     list.append(temp)
    # count = db.batchInsert(sql, list)
    # print count
    # print list

    def tearDown(self):
        print '======================== finish ======================================'


if __name__ == '__main__':
    unittest.main()
