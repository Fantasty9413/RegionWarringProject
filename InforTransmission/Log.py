#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/20 14:15
# @Author: Fantasty9413
# @File  : Log.py

import logging

# #   初始化日志对象
# logging.basicConfig(
# #   日志级别
# level = logging.DEBUG,
# # 日志格式
# # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
# format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# # 打印日志的时间
# datefmt = '%a, %d %b %Y %H:%M:%S',
# # 日志文件存放的目录（目录必须存在）及日志文件名
# filename = './Log/report.log',
# # 打开日志文件的方式
# filemode = 'a'      #a = add 追加, w = write 新建文件
# )
#
# # logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#
# logging.disable(logging.DEBUG)       # 禁用相应级别及其以下的日志

# Report Log -- 记录报告日志
# 定义文件
file_report = logging.FileHandler(filename='./Log/report.log', mode='a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
file_report.setFormatter(fmt)

# 定义日志
logger_report = logging.Logger(name='Report Log', level=logging.DEBUG)
logger_report.addHandler(file_report)

# 写日志
# logger_report.error(msg='exception log test')
# logger_report.log(msg='exception log test', level=50)


# Exception Log -- 记录异常日志
# 定义文件
file_exception = logging.FileHandler(filename='./Log/exception.log', mode='a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
file_exception.setFormatter(fmt)

# 定义日志
logger_exception = logging.Logger(name='Exception Log', level=logging.DEBUG)
logger_exception.addHandler(file_exception)

# 写日志
# logger_exception.info('exception log test')
