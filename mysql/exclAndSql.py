#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd
import pymysql

# 打开Excel文件 win下注意\改成/
workbook = xlrd.open_workbook('C:/Users/qidima/Desktop/model_data.xlsx')

# Connect to the database
ip = 'localhost'
user = 'root'
db = "usedcar"
password = '123456'
charset = 'gbk'

connection = pymysql.connect(host=ip,
                             user=user,
                             password=password,
                             db=db,
                             charset=charset,
                             cursorclass=pymysql.cursors.DictCursor)
# 获取游标
cursor = connection.cursor()


# 批量修改表
def batchUpdate(sql, list):
    try:
        cursor.executemany(sql, list)
        connection.commit()
        print('----------------------update sql is success-----------------------------')
    except Exception as e:
        connection.rollback()
        print(str(e))


# 根据工作表索引获取工作表
def packageDataList():
    sheet = workbook.sheet_by_index(0)  # 第一张表
    column_std = sheet.col_values(0, 1, 2005)
    column_id = sheet.col_values(1, 1, 2005)
    dateList = []
    index = 0
    # 拼接git
    for id in column_id:
        list = []
        list.append(str(column_std[index]))
        list.append(int(id))
        dateList.append(list)
        index = index + 1
    return dateList


if __name__ == '__main__':
    list = packageDataList()
    batch_sql = 'update sc_model set std_name = %s  WHERE id = %s '
    batchUpdate(batch_sql, list)
    connection.close()
