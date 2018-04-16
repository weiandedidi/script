#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site:  
@software: PyCharm 
@file: test.py 
@time: 2018/3/1 16:12 
"""
import requests
import time
from bs4 import BeautifulSoup


def get_doctor_schedule():
    # url
    url_base = 'https://api.zwjk.com/export/ui/doct/list_1_7_4',
    date = {
        'executionId': 'process%3A032742a4-383e-4ce6-af5b-aa8d37485a30',
        'pageFormKey': '1-7-4',
        'ucUiFlowId': '98db3dd2-b2d2-11e6-a249-525400644ee2',
        'stepId': 'F_1-7-4'
    }

    unsign = ''
    for key in date:
        # print date[key]
        unsign = unsign + key + '=' + date[key] + '&'
    unsign = unsign[0: -1]
    print unsign

    #
    # strxx = 'executionId=process:032742a4-383e-4ce6-af5b-aa8d37485a30&noticeStr=' \
    #         + str(randstr) \
    #         + '&pageFormKey=1-7-4&stepId=F_1-7-4&timestamp=' \
    #         + str(millis) + \
    #         '&ucUiFlowId=98db3dd2-b2d2-11e6-a249-525400644ee2'


if __name__ == '__main__':
    get_doctor_schedule()
