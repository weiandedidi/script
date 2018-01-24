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

# 设置代理
proxies = {
    "https": "http://41.118.132.69:4433"
}
r = requests.post("http://httpbin.org/post", proxies=proxies)
print r.text
