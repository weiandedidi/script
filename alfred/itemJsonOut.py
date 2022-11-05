#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: maqidi 
@license: Apache Licence  
@site:  
@software: PyCharm 
@file: testPrint
@time: 2022/10/27 下午7:24 
"""
import json

from workflow import Workflow3
import sys


# 通过 script filter输出的是json格式的，需要是item类
def main(wf):
    args = wf.args
    # 输出item的list的文本，并未json 的list项目，并且格式是Unicode，需要u进行规避
    wf.add_item(title=u'名字', subtitle=args[0], type="largetext", largetext=u'你好', valid=True)
    # wf.getvar(args[0])
    wf.send_feedback()


if __name__ == '__main__':
    dict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
    wf = Workflow3()
    sys.exit(wf.run(main))
