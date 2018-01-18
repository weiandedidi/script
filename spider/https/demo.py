#!/usr/bin/python
# -*- coding: utf-8 -*-

x = int(raw_input("x:"))
y = int(raw_input("y:"))
z = int(raw_input("z:"))
a = {"x":x,"y":y,"z":z}
print '--------分割线--------'
for w in sorted(a, key=a.get):
    print w, a[w]