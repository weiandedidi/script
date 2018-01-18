#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

response = urllib2.urlopen("https://www.che168.com/Handler/ScriptCarList_V1.ashx?seriesGroupType=2&needData=2&bid=271")
print response.read().decode("gbk").encode("utf-8")
# 中文乱码调整

# Proxy（代理）的设置
# import urllib2
#
# enable_proxy = True
# proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib2.ProxyHandler({})
# if enable_proxy:
#     opener = urllib2.build_opener(proxy_handler)
# else:
#     opener = urllib2.build_opener(null_proxy_handler)
# urllib2.install_opener(opener)
