#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: maqidi 
@license: Apache Licence  
@site:  
@software: PyCharm 
@file: directOut
@time: 2022/10/27 下午8:18 
"""

from workflow import Workflow3
import sys


# 直接输出文本
def main(wf):
    today_str = '1024'

    # wf.add_item('1222', today_str, '2021', valid=True)
    # 这是直接输出的文本，action中的run script 输出到控制台的字段，无需格式。
    sys.stdout.write("我是牛逼人")
    # wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
