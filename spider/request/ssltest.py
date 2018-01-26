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
# 不安全的证书认证 exceptions.SSLError: HTTPSConnectionPool(host='2sc.sohu.com', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, u'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:661)'),))
r = requests.get('https://www.163.com/', verify=True)
# 不安全的证书不认证 ok通过
r = requests.get('https://www.163.com/', verify=False)
# r = requests.get('https://github.com', verify=False)
print r.text
