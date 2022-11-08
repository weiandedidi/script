#!/usr/bin/python 
# -*- coding: UTF-8 -*-
""" 
@version: v1.0 
@author: maqidi 
@license: Apache Licence  
@site:  
@software: PyCharm 
@file: ocr
@time: 2022/10/28 下午11:33 
"""
import base64
import json
import os
import sys
import time
from enum import Enum

import cv2
import config
from PIL import Image, ImageGrab
import numpy as np
import requests

'''
1. 图片粘贴到剪切板中。
2. 图片转码为base64  并且去掉头部的 data:image/jpg;base64,
3. 使用存储百度的请求token，30天刷新一次
4. 请求百度的通用图像识别接口
'''


class ImageType(Enum):
    """
    枚举类，用于标定是否有
    """
    noImage = 1
    tooLarge = 2
    hasImage = 3


class imageObj:
    hasImage = 1
    base64Code = ''

    # 定义基本属性
    def __init__(self, hasImage, base64Code):
        self.hasImage = hasImage
        self.base64Code = base64Code


def convert_image_base64():
    """
    详见
    1. 知乎 python图像操作 https://zhuanlan.zhihu.com/p/383156319 需要安装pillow包
    2. image转为数据 https://blog.csdn.net/weixin_36670529/article/details/107634869  需要安装 opencv-python包
    :return:
    """
    image = ImageGrab.grabclipboard()
    if image is None:
        return imageObj(ImageType['noImage'], None)
    # 像素转内存大小
    list = image.size
    length = list[0]
    weight = list[1]
    size = length * weight * 3
    # 字节不超过4m
    if size > 4194304:
        return imageObj(ImageType['tooLarge'], None)
    # 转化成numpy数组
    image_arr = np.array(image)
    # 数组转为byte
    data = cv2.imencode('.jpg', image_arr)[1]
    image_bytes = data.tobytes()
    # byte转为base64
    image_base4 = base64.b64encode(image_bytes).decode('utf8')
    return imageObj(ImageType['hasImage'], image_base4)


def get_baidu_ocr_data():
    imageObj = convert_image_base64()
    if imageObj.hasImage == ImageType['noImage']:
        return "no image get !!!"
    if imageObj.hasImage == ImageType['tooLarge']:
        return "image to large than 4m !!!"
    # 请求百度获取ocr结果
    response = request_baidu_orc(imageObj.base64Code)
    # 解析百度的ocr结果
    if response.status_code == 200:
        result_json = json.loads(response.text)
        return parse_baidu_ocr_result(result_json)
    else:
        return 'baidu Request failed!'


def parse_baidu_ocr_result(response_json):
    """
    解析报百度返回的list数据，进行使用换行符进行拼接
    :param response_json:
    :return:
    """
    words_result_num = response_json['words_result_num']
    if words_result_num is None or words_result_num == 0:
        return "ocr parse no word !!!"
    word_result_list = response_json['words_result']
    words_list = list(map(lambda word: word['words'], word_result_list))
    split_dot = '\n'
    return split_dot.join(words_list)


def request_baidu_orc(image_base4):
    response = requests.post(
        url=config.BAIDU_OCR_API,
        params={"access_token": get_baidu_token()},
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "image": image_base4,
        })
    return response


def get_baidu_token():
    """
    获取百度的token
    :return:
    """
    if ((not os.path.exists('./baidu_api_token.json'))
            or (int(time.time() - os.stat("./baidu_api_token.json").st_mtime) >= 259200)):

        return request_baidu_token()
    else:
        with open("./baidu_api_token.json", 'r') as json_file:
            api_message_json = json.load(json_file)
            if 'access_token' in api_message_json:
                return api_message_json.get('access_token')
            else:
                return request_baidu_token()


def request_baidu_token():
    response = requests.get(config.BAIDU_GET_TOKEN_URL).json()
    if ('access_token' in response):
        with open("./baidu_api_token.json", "w") as json_file:
            json.dump(response, json_file)
        token = response['access_token']
        return token
    else:
        print("Error: " + response['error_description'])
        sys.exit(0)


if __name__ == '__main__':
    # 1. 获取百度的ocr结果
    result = get_baidu_ocr_data()
    # 2. 打印到剪切板
    sys.stdout.write(result)
