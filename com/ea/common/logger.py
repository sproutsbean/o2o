#!usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@author:user 
@file: logger.py 
@time: 2017/11/15 
"""
import logging.handlers
import os

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'log/log.txt')
fh = logging.FileHandler(log_path)
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)