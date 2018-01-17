#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@author:user 
@file: chinese.py 
@time: 2018/01/17 
"""

import random


def GBK2312():
    strs = ""
    for i in range(random.randint(2, 10)):
        head = random.randint(0xb0, 0xf7)
        body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
        val = f'{head:x}{body:x}'
        strs = strs + bytes.fromhex(val).decode('gb2312')
    print(strs)


GBK2312()
