#!/usr/bin/env python
# encoding: utf-8
"""
@version: v1.0
@author: qidima
@license: Apache Licence
@contact: weiandedidi@qq.com
@site: https://github.com/weiandedidi/script
@software: PyCharm
@file: post.py
@time: 2018/1/24 17:49
"""

import requests
# 认证
# r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
# 不认证
r = requests.get('https://www.sina.com.cn/', verify=False)
# r = requests.get('https://github.com', verify=False)
print r.text
