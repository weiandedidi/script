#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: mysqlUtil.py 
@time: 2018/2/1 16:25

1、执行带参数的ＳＱＬ时，请先用sql语句指定需要输入的条件列表，然后再用tuple/list进行条件批配
2、在格式ＳＱＬ中不需要使用引号指定数据类型，系统会根据输入参数自动识别
3、在输入的值中不需要使用转意函数，系统会自动处理
"""

import pymysql
import sys
from DBUtils.PooledDB import PooledDB
from pymysql.cursors import DictCursor

reload(sys)
sys.setdefaultencoding('utf-8')


class Config(object):
    """数据库链接的参数"""
    DBHOST = '10.11.172.233'
    DBPORT = '3306'
    DBUSER = 'wanjiang'
    DBPWD = 'wanjiang0310'
    DBCHAR = 'gbk'


class Mysql(object):
    """
    MYSQL数据库对象，负责产生数据库连接 , 此类中的连接采用连接池实现获取连接对象：conn = Mysql.getConn()
            释放连接对象;conn.close()或del conn
    """
    # 连接池对象
    __pool = None

    def __init__(self):
        # 数据库构造函数，从连接池中取出连接，并生成操作游标
        try:
            self._conn = Mysql.__getConn()
            self._cursor = self._conn.cursor()
        except Exception, e:
            error = 'Connect failed! ERROR (%s): %s' % (e.args[0], e.args[1])
            print error
            sys.exit()

    @staticmethod
    def __getConn():
        """
        @summary: 静态方法，从连接池中取出连接
        @return MySQLdb.connection
        """
        if Mysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20,
                              host=Config.DBHOST,
                              port=Config.DBPORT,
                              user=Config.DBUSER,
                              passwd=Config.DBPWD,
                              db=Config.DBNAME,
                              use_unicode=False,
                              charset=Config.DBCHAR,
                              cursorclass=DictCursor)
        return __pool.connection()

