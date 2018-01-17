#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:user 
@file: test.py 
@time: 2018/01/03 
"""

import requests


r = requests.get("http://service.o2ojr.eascs.com/brand/index")
print(r.status_code)