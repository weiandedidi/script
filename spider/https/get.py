#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2


values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login"
# url = "https://www.sohu.com"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl
