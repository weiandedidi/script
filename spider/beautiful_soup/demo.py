#!/usr/bin/python
# encoding: utf-8  
""" 
@version: v1.0 
@author: qidima 
@license: Apache Licence  
@contact: weiandedidi@qq.com 
@site: https://github.com/weiandedidi/script 
@software: PyCharm 
@file: demo.py 
@time: 2018/1/25 10:31 
"""
import bs4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, "html.parser")
# print soup.prettify()
# 1. 识别标签，如下方法，只识别第一条符合的。
print soup.title
print soup.a
print soup.p
print soup.head
print '----------------------------------------'
# 识别属性 soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称
print soup.head.name
print soup.name
# 打印标签所有的属性.attrs
print soup.p.attrs
# 打印指定属性
print soup.p['name']
print soup.p.get('name')
# 修改属性
soup.p['name'] = 'ok'
print soup.p.get('name')
# 删除属性
del soup.p['name']
print soup.get('name')
# 2. NavigableString 可操作字符串
xsxs = soup.p.string
print type(xsxs)
print '----------------------------------------'
# 3. BeautifulSoup 表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag
print type(soup.name)
xxx = str(123)
print type(xxx)
print '----------------------------------------'

# 4. Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容仍然不包括注释符号，但是如果不好好处理它，可能会对我们的文本处理造成意想不到的麻烦。

print soup.a
print soup.a.string
print type(soup.a.string)
print '----------------------------------------'
if type(soup.a.string) == bs4.element.Comment:
    print soup.a.string
print '----------------------------------------'
# 5.选择器
print soup.select('title')
print type(soup.select('title'))

