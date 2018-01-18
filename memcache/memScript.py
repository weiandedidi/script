#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pymemcache

# 链接memmcahe的client
import time
from pymemcache.client import Client

client_one = Client(('10.16.56.251', 11211))
client_two = Client(('10.18.34.17', 11211))
client_three = Client(('10.11.173.23', 11211))
client_four = Client(('10.11.173.23', 11212))


# client.set('some_key', 'some_value')
# result = client.get('some_key')


def add_data(value):
    bbb = json.dumps(value)
    return bbb


if __name__ == '__main__':
    # key = 'xxxx.xxx'
    key = '/chip/sohuIndex.shtml'
    # data = '{ "left": [ { "t": "呆萌小狮标致307三厢舒适版 售价2万起", "turl": "//2sc.sohu.com/auto1-307sx/?pvid=264c5e4f", "p": "//2sc.sohu.com/auto1-307sx/?pvid=264c5e4f", "purl": "//5b0988e595225.cdn.sohucs.com/images/20171101/836b112a423d488580ef6075d2fb6634.png" }, { "t": "全地形SUV路虎第四代发现 售价43.6W", "turl": "//2sc.sohu.com/sccarnew/openChejiandingReport.shtml?detailReport=https://www.chejianding.com/o/partner/sohuBuy/U0FMQU4yRjQ5QkE1NjMyMjY=?trimm=%25E8%25B7%25AF%25E8%2599%258E%25E7%25AC%25AC%25E5%259B%259B%25E4%25BB%25A3%25E5%258F%2591%25E7%258E%25B02011%25E6%25AC%25BE3.0L%2520SD%2520HSE%2520%25E6%259F%25B4%25E6%25B2%25B9%25E7%2589%2588&pvid=bea7161b/?pvid=264c5e4f", "p": "//2sc.sohu.com/sccarnew/openChejiandingReport.shtml?detailReport=https://www.chejianding.com/o/partner/sohuBuy/U0FMQU4yRjQ5QkE1NjMyMjY=?trimm=%25E8%25B7%25AF%25E8%2599%258E%25E7%25AC%25AC%25E5%259B%259B%25E4%25BB%25A3%25E5%258F%2591%25E7%258E%25B02011%25E6%25AC%25BE3.0L%2520SD%2520HSE%2520%25E6%259F%25B4%25E6%25B2%25B9%25E7%2589%2588&pvid=bea7161b/?pvid=264c5e4f", "purl": "//5b0988e595225.cdn.sohucs.com/images/20171031/53c07267c5044bef82b0711e20b60dea.jpeg" }, { "t": "大众最具动感的双门轿跑车 尚酷仅售13.68万", "turl": "//2sc.sohu.com/auto1-scirocco1/?pvid=264c5e4f", "p": "//2sc.sohu.com/auto1-scirocco1/?pvid=264c5e4f", "purl": "//5b0988e595225.cdn.sohucs.com/images/20171031/f6ca6e5346e143b586023e6b434737cf.jpeg" } ], "right1": [ { "t": "准新车", "turl": "//2sc.sohu.com/buycar/a0b0c0d0e0f0g4h0j0k0m0n0/?pvid=49334f21" }, { "t": "大众", "turl": "//2sc.sohu.com/auto-volkswagen/a0b0c0d0e0f0g0h0j0k0m0n0/?pvid=49334f21" }, { "t": "帮我卖车", "turl": "//2sc.sohu.com/sellCarWeb/sellPerCar/?pvid=49334f21" }, { "t": "白菜价买好车", "turl": "//2sc.sohu.com/buycar/a0b0_10c0d0e0f0g0h0j0k0m0n0/?pvid=49334f21" }, { "t": "商家发车", "turl": "//2sc.sohu.com/ctb/?pvid=49334f21" }, { "t": "我要估价", "turl": "//2sc.sohu.com/evaluate/evaluateIndex/?pvid=49334f21" }, { "t": "MPV", "turl": "//2sc.sohu.com/buycar/a7b0c0d0e0f0g0h0j0k0m0n0/?pvid=49334f21" }, { "t": "怎样卖车最划算", "turl": "//2sc.sohu.com/sellCarWeb/sellPerCar/?pvid=49334f21" }, { "t": "5年的车能卖多少钱", "turl": "//2sc.sohu.com/evaluate/evaluateIndex/?pvid=49334f21" }, { "t": "商家发车", "turl": "//2sc.sohu.com/ctb/?pvid=49334f21" }, { "t": "本地热门车", "turl": "//2sc.sohu.com/buycar/?pvid=49334f21" } ] }'
    # data_u = data.decode("utf-8")
    # value = data_u.encode("gbk")
    # client_one.set(key, value)
    # data = 1
    # client_one.set(key, data, 2)
    # num = client_one.get(key)
    # time.sleep(3)
    # print num
    # client_one.replace(key, 3)
    # time.sleep(5)
    temp = client_three.get('MSG_IDENTIFY_CODE|15120065502')
    f = client_four.get('MSG_IDENTIFY_CODE|15120065502')
    # client_two.set(key, value)
    # client_two.set(key, data)
    client_three.set('MSG_IDENTIFY_CODE|15120065502', 456123, 600)
    heh = client_three.get('MSG_IDENTIFY_CODE|15120065502')
    print temp
    print f
    print heh
