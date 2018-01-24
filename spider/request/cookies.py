#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: qidima
@license: Apache Licence
@contact: weiandedidi@qq.com
@site: https://github.com/weiandedidi/script
@software: PyCharm
@file: get.py
@time: 2018/1/24 17:52
"""

import requests

url = 'http://httpbin.org/cookies'
# 添加cookie值
cookies = dict(xx_xx='working')
r = requests.get(url, cookies=cookies)
print r.text