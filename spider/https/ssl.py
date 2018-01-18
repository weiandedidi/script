#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
r = requests.get('https://kyfw.12306.cn/otn/', verify=false)
print r.text
