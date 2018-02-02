#!/usr/bin/env python  
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: mysqlTest.py 
@time: 2018/2/2 14:13 
"""
import unittest
from mysql.utils.mysqlutil import *


# 创建mysql连接
db = Mysql()


class testUtils(unittest.TestCase):

    def setUp(self):
        pass

    def testSelect(self):
        pass
        # sql = 'select * from user'
        # one = db.getAll(sql)
        # print one

    def testInsert(self):
        pass

    def testUpdate(self):
        pass

    def testBatchInsert(self):
        sql = 'insert into user(name,departId,age)values(%s,%s,%s)'
        list = []
        for i in range(1, 50):
            temp = ('name' + str(i), 2, i)
            list.append(temp)
        count = db.batchInsert(sql, list)
        print count
        print list

    def tearDown(self):
        print '======================== finish ======================================'


if __name__ == '__main__':
    unittest.main()
